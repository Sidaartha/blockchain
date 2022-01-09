"""
	routs.py
	Created at: 2022-01-09
	Author: Sidaartha Reddy
"""

from flask import Blueprint
import controller

main = Blueprint("main", __name__)

main.add_url_rule(
    rule="/mine_block",
    view_func=controller.mine_block,
    methods=["GET"],
)
main.add_url_rule(
    rule="/get_chain",
    view_func=controller.get_chain,
    methods=["GET"],
)
main.add_url_rule(
    rule="/is_valid",
    view_func=controller.is_valid,
    methods=["GET"],
)
