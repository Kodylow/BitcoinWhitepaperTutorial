import hashlib
import multiprocessing

# Function to generate random block headers
def generate_block_header():
    nonce = 0
    prev_block_hash = '0000000000000000000000000000000000000000000000000000000000000000'
    timestamp = 1234567890
    merkle_root = 'abcd1234'
    block_header = f'{prev_block_hash}{merkle_root}{timestamp}{nonce}'
    return block_header

# Function to compute SHA256 hash of a block header
def compute_sha256(block_header):
    sha256 = hashlib.sha256()
    sha256.update(block_header.encode())
    return sha256.hexdigest()

# Function to find a SHA256 hash below a set difficulty
def find_hash(difficulty):
    num_blocks_found = 0
    while True:
        block_header = generate_block_header()
        sha256 = compute_sha256(block_header)
        if sha256[:difficulty] == '0' * difficulty:
            print(f'Process {multiprocessing.current_process().name}: Found block {num_blocks_found} with header {block_header} and hash {sha256}')
            num_blocks_found += 1

# Start 3 processes to find the hash
if __name__ == '__main__':
    difficulty = 5
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=find_hash, args=(difficulty,), name=f'Process-{i}')
        processes.append(process)
        process.start()

    for process in processes:
        process.join()