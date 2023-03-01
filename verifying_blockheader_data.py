### Getting Bitcoin Block Header Data

# You can use the Esplora API to grab these from the internet. 
# The route is `www.blockstream.info/api/blocks/${block_height}` where block_height is the first of 10 sequential block headers you want to get.

# if you've never sent http requests with python to get internet data before, the format is:
    # data = requests.get('route_youre_querying')

import requests
import json
# TODO: Write a function get_10_prev_blocks that takes an argument, blockheight, and gets that block header and the 9 previous block headers from the bitcoin blockchain.
# So if you call get_10_prev_blocks(100), your function should return the block headers from block 100 to block 91

def get_10_prev_blocks(blockheight):
    # YOUR CODE HERE
    block_headers = 'fix me'
    
    # Print your returned block_headers JSON nicely with json.dumps()
    for i in in block_headers:
        print(json.dumps(block_headers, indent=2))
    return block_headers

# TESTS: do not change
block_headers_100_to_91 = get_10_prev_blocks(100)
assert len() == 10
block100_header = {
    "id": "000000007bc154e0fa7ea32218a72fe2c1bb9f86cf8c9ebf9a715ed27fdb229a",
    "height": 100,
    "version": 1,
    "timestamp": 1231660825,
    "tx_count": 1,
    "size": 215,
    "weight": 536,
    "merkle_root": "2d05f0c9c3e1c226e63b5fac240137687544cf631cd616fd34fd188fc9020866",
    "previousblockhash": "00000000cd9b12643e6854cb25939b39cd7a1ad0af31a9bd8b2efe67854b1995",
    "mediantime": 1231656204,
    "nonce": 1573057331,
    "bits": 486604799,
    "difficulty": 1
  }
assert block_headers_100_to_91[0] == block100_header



### Verifying Bitcoin Block Headers
from hashlib import sha256

# Part A
# TODO: Write a function, sha256d, that hashes an input twice with sha256, returning the final digest.
# check out the 
def sha256d(data):
    pass


# Part B
# TODO: Write a function, flip_endianness, which takes a hex string input in big/little endian and flips returns a hex string with the flipped byte ordering
def flip_endianness(data):
    pass


# TODO:  Write a function, format_blockheader, which takes a dictionary of blockheader data (returned by Esplora) as input and outputs a single little endian hex string properly formatted per the instructions in main.py
def format_blockheader(blockheader):
    pass


# Part C
# TODO: Write a function, verify_bitcoin_block, that takes 2 sequential block headers, block and prev_block, and verifies that block builds on the first block. Return True if the "previousblockhash" field in block matches the SHA256D output of prev_block
def verify_bitcoin_block(block, prev_block):

    # YOUR CODE HERE
    # pull these fields off the prev_block json and encode them as LITTLE ENDIAN BYTES
    version = flip_endianness(prev_block["version"])
    prev_hash = 'fixme'
    merkle_root = 'fixme'
    time = 'fixme'
    bits = 'fixme'
    nonce = 'fixme'

    # Concatenate all of the fields together in EXACTLY this order
    preimage = version + prevhash + merkle_root + time + bits + nonce

    # Then find the sha256d output as hexdigest

    # and verify block["previousblockhash"] == hexdigest
    if fix_me:
        return True
    return False


# TESTS: Do not change
blocks = block_headers_100_to_91
for i in range(len(blocks) - 2):
    assert verify_bitcoin_block(blocks[i], blocks[i + 1])

print("Done with Final Exercise!! Congratulations, you're a Hashing Wizard!!!")
