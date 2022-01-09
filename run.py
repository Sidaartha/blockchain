"""
	run.py
	Created at: 2022-01-09
	Author: Sidaartha Reddy
"""

from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
