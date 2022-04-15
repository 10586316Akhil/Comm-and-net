# server.py
from flask import Flask

SECRET_MESSAGE = "test message"
app = Flask("CommApp_Flask")

@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE