import hashlib
import json
from time import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = self.create_block(0, "0", int(time()), "Genesis Block")
        self.chain.append(genesis_block)

    def create_block(self, index, previous_hash, timestamp, data):
        block = Block(index, previous_hash, timestamp, data, self.calculate_hash(index, previous_hash, timestamp, data))
        return block

    def calculate_hash(self, index, previous_hash, timestamp, data):
        value = f"{index}{previous_hash}{timestamp}{data}"
        return hashlib.sha256(value.encode()).hexdigest()

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = self.create_block(latest_block.index + 1, latest_block.hash, int(time()), data)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            if current_block.hash != self.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Example usage
blockchain = Blockchain()
blockchain.add_block("First block after Genesis")
blockchain.add_block("Second block after Genesis")

print("Blockchain is valid:", blockchain.is_chain_valid())

for block in blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print("\n")
