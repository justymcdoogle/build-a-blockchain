import hashlib
import json
from time import time
from uuid import uuid4



class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        creates a new block and adds it to the chain
        :param proof: <int> The proof given by the Proof of Work Algorithm
        :param previous_hash: (Optional) <str> Hash of previous block
        return: <dict> New Block
        """
        
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined block
        :param sender: <str> Address of the sender
        :param recipient: <str> Address of the recipient
        :param amount: <int> amount
        :return: <int> The index of the block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

        def proof_of_work(self, last_proof):
            """
            Simple proof of work Algorithm:
            - Find number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
            - p is the previous proof, and p' is the new proof
            :param last_proof: <int>
            :return: <int>
            """

            proof = 0
            while self.valid_proof(last_proof, proof) is False:
                proof += 1

            return proof

    @property
    def last_block(self):
        # returns the last block in the chain
        return self.chain[-1]

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the proof: does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> previous proof
        :param proof: <int> current Proof
        :return <bool> true if correct, false if not.
        """ 

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"



        # we must make sure the dictionary is ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
