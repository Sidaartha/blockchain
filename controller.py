"""
	controller.py
	Created at: 2022-01-09
	Author: Sidaartha Reddy
"""

from flask import jsonify

from blockchain import Blockchain

blockchain = Blockchain()


def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block["proof"]
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {
        "message": "Congratulations, you just mined a block!",
        "index": block["index"],
        "timestamp": block["timestamp"],
        "proof": block["proof"],
        "previous_hash": block["previous_hash"],
    }
    return jsonify(response), 200


def get_chain():
    response = {"chain": blockchain.chain, "length": len(blockchain.chain)}
    return jsonify(response), 200


def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {"message": "All good. The Blockchain is valid."}
        return jsonify(response), 200

    response = {"message": "Houston, we have a problem. The Blockchain is not valid."}
    return jsonify(response), 400
