"""
	app.py
	Created at: 2022-01-09
	Author: Sidaartha Reddy
"""

from flask import Flask
from routs import main

app = Flask(__name__)

app.register_blueprint(main)
