"""
	controller.py
	Created at: 2022-01-09
	Author: Sidaartha Reddy
"""
from uuid import uuid4

from flask import jsonify, request

from blockchain import Blockchain

node_address = str(uuid4()).replace("-", "")
blockchain = Blockchain()


def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block["proof"]
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.add_transaction(sender=node_address, receiver="SID", amount=1)
    block = blockchain.create_block(proof, previous_hash)
    response = {
        "message": "Congratulations, you just mined a block!",
        "index": block["index"],
        "timestamp": block["timestamp"],
        "proof": block["proof"],
        "previous_hash": block["previous_hash"],
        "transactions": block["transactions"],
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


def add_transaction():
    json = request.get_json()
    transaction_keys = ["sender", "receiver", "amount"]
    if not all(key in json for key in transaction_keys):
        return "Some elements of the transation are missing", 400

    index = blockchain.add_transaction(
        {
            "sender": json["sender"],
            "receiver": json["receiver"],
            "amount": json["amount"],
        }
    )
    response = {"message": f"This transaction will be added to the block {index}"}
    return jsonify(response), 201


def connect_node():
    json = request.get_json()
    nodes = json.get("nodes")
    if not nodes:
        return "No nodes", 400

    for node in nodes:
        blockchain.add_node(node)
    response = {
        "message": f"All the nodes are now connected",
        "total_nodes": list(blockchain.nodes),
    }
    return jsonify(response), 201


def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {"message": "The chain was replaced by the longest one."}
    else:
        response = {"message": "All good. The chain is the longest one."}
    return jsonify(response), 200
