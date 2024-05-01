import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

def print_block(block):
    print("Index: ", block.index)
    print("Previous Hash: ", block.previous_hash)
    print("Timestamp: ", block.timestamp)
    print("Data: ", block.data)
    print("Hash: ", block.hash)
    print("\n")

def main():
    # Create the genesis block
    genesis_block = create_genesis_block()
    print_block(genesis_block)

    # Simulate blockchain
    blockchain = [genesis_block]
    previous_block = genesis_block
    data = "Hello, Blockchain!"
    for i in range(1, 20):
        block_to_add = create_new_block(previous_block, data)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        print_block(block_to_add)
        print("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print("Hash: {}\n".format(block_to_add.hash))

    # Function to generate a blog post title
    def generate_blog_title(topic):
        return f"{topic} - Insights from a Sage Code Hooter"

    # Example usage
    blog_topic = "Blockchain Development with Python"
    print(generate_blog_title(blog_topic))

if __name__ == "__main__":
    main()
