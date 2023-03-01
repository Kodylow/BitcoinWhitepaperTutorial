import hashlib
import time
from threading import Thread

class Block:
    def __init__(self, version, prev_hash, merkleroot, timestamp, bits, nonce):
        self.version = version
        self.prev_hash = prev_hash
        self.merkleroot = merkleroot
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_data = f"{self.version}{self.prev_hash}{self.merkleroot}{self.timestamp}{self.bits}{self.nonce}".encode('utf-8')
        return hashlib.sha256(hash_data).hexdigest()


class Blockchain:
    def __init__(self, difficulty):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

class Miner:
    def __init__(self, name, blockchain):
        self.name = name
        self.nonce = 0
        self.blockchain = blockchain

    def mine(self, block_data):
        target = '0' * self.blockchain.difficulty
        while True:
            timestamp = time.time()
            new_block = Block(len(self.blockchain.chain), block_data, timestamp, '')
            hash_data = f"{new_block.index}{new_block.data}{new_block.timestamp}".encode('utf-8')
            hash_result = hashlib.sha256(hash_data).hexdigest()
            if hash_result[:self.blockchain.difficulty] == target:
                new_block.previous_hash = self.blockchain.get_latest_block().hash
                new_block.hash = new_block.calculate_hash()
                print(f"{self.name} mined block with nonce {self.nonce} and hash {new_block.hash}")
                self.blockchain.add_block(new_block)
                break
            self.nonce += 1

genesis_info = {
    "version": 1,
    "merkleroot": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
    "time": 1231006505,
    "nonce": 2083236893,
    "bits": "1d00ffff",
    "previous_hash": "0000000000000000000000000000000000000000000000000000000000000000",
}

version = genesis_block['version']
prev_hash = genesis_block['previous_hash']
merkleroot = genesis_block['merkleroot']
timestamp = genesis_block['time']
bits = genesis_block['bits']
nonce = genesis_block['nonce']

genesis_block = Block(version, prev_hash, merkleroot, timestamp, bits, nonce)

network_blockchain = Blockchain(5)

alice = Miner("Alice", network_blockchain, 8000)
bob = Miner("Bob", network_blockchain, 8001)
charlie = Miner("Charlie", network_blockchain, 8002)

miners = [alice, bob, charlie]
for miner in miners:
    t = Thread(target=miner.mine)
    t.start()