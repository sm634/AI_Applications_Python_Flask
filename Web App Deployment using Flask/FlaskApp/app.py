from flask import Flask
from flask import jsonify
from requests import request

app = Flask(__name__)

"""Normal print based on HTML."""
# @app.route('/')
# def hello_world():
#     return "<b> A test Flask application in action! <b>"

""""Json output.""""
# @app.route('/')
# def index():
#     return {"message": "hello world!"}


"""Uing the jsonify() methos"""
@app.route('/')
def index():
    return jsonify(message="hello world")

"""Specify the get method implicitly (@app.route() automatically does this.)"""
@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

"""Specify the get method explicitly."""
@app.route("/health", methods=["GET"])
def health():
    return jsonify(dict(status="OK")), 200


"""Custom Routes: Example"""
@app.route("/health", methods=["GET", "POST"])

def health():
    if request.method == "GET": return jsonify(statsu="OK", method="GET"), 200

    if request.method == "POST": return jsonify(status="OK", method="POST"), 200


# Example URL: http://localhost:5000?course=capstone&rating=10

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    course = request.args["course"]  #gets the value associated with 'course' in the example url. 
    rating = request.args.get("rating")  #gets the value assocaited with rating in the example url.
    return {"message": f"{course} with rating {rating}"}
