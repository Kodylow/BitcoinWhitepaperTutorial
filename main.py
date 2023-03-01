import hashlib
import json
import requests
import subprocess


def get_block_header_by_height(height):
    block_hash = subprocess.check_output(f'bitcoin-cli getblockhash {height}', shell=True).decode().strip()
    # strip leading b and trailing \n
    print('block_hash: ', block_hash)
    block_header = subprocess.check_output(f'bitcoin-cli getblockheader {block_hash}', shell=True).decode()
    return block_header


def sha256(x):
    return bytes(hashlib.sha256(x).digest())


def sha256d(x):
    return sha256(sha256(x))


def hash_decode(x):
    return bytes.fromhex(x)[::-1]


def merklize(tx_hash, merkle_branch, pos):
    """Return calculated merkle root."""
    h = hash_decode(tx_hash)
    merkle_branch_bytes = [hash_decode(item) for item in merkle_branch]
    data = {'name': tx_hash, 'children': []}
    for item in merkle_branch_bytes:
        if pos & 1:
            inner_node = item + h
            data = {
                'name': sha256d(inner_node)[::-1].hex(),
                'children': [
                    {
                        'name': item.hex(),
                    },
                    data,
                ],
            }
        else:
            inner_node = h + item
            data = {
                'name': sha256d(inner_node)[::-1].hex(),
                'children': [
                    data,
                    {
                        'name': item.hex(),
                    },
                ],
            }
        h = sha256d(inner_node)
        pos >>= 1

    return {
        'calculated_merkle_root': h[::-1].hex(),
        'tree': data,
    }


from anytree import Node, RenderTree


def build_tree(node_data):
    node_name = node_data["name"]
    node_children = node_data.get("children", [])
    node = Node(node_name)
    for child in node_children:
        child_node = build_tree(child)
        child_node.parent = node
    return node


def print_hash_tree(tree):
    root_data = tree["tree"]
    root_node = build_tree(root_data)
    for pre, _, node in RenderTree(root_node):
        print(f"{pre}{node.name}")


# user inputs a txid
txid = input('Enter the txid for the merkle_proof: ').strip()

merkle_proof = requests.get(
    f"https://blockstream.info/api/tx/{txid}/merkle-proof").text
merkle_dict = json.loads(merkle_proof)

print("Merkle Proof:\n")
print(json.dumps(merkle_dict, indent=4))

merkle_tree = merklize(txid, merkle_dict["merkle"], int(merkle_dict["pos"]))
print("\nCalculated Merkle Tree:\n")
print_hash_tree(merkle_tree)

local_block_header = get_block_header_by_height(merkle_dict["block_height"])
print("\nBlockheader from our node: ", local_block_header)

print("\nCalculated Merkle Root matches Local Blockheader's Merkle Root: ", merkle_tree["calculated_merkle_root"] == json.loads(local_block_header)["merkleroot"])