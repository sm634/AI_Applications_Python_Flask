from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)

"""Normal print based on HTML."""
# @app.route('/')
# def hello_world():
#     return "<b> A test Flask application in action! <b>"

"""Json output."""
# @app.route('/')
# def index():
#     return {"message": "hello world!"}


"""Uing the jsonify() methos"""
# @app.route('/')
# def index():
#     return jsonify(message="hello world")

# """Specify the get method implicitly (@app.route() automatically does this.)"""
# @app.route("/health")
# def health():
#     return jsonify(dict(status="OK")), 200

# """Specify the get method explicitly."""
# @app.route("/health", methods=["GET"])
# def health():
#     return jsonify(dict(status="OK")), 200


# """Custom Routes: Example"""
# @app.route("/health", methods=["GET", "POST"])

# def health():
#     if request.method == "GET": return jsonify(statsu="OK", method="GET"), 200

#     if request.method == "POST": return jsonify(status="OK", method="POST"), 200


# # Example URL: http://localhost:5000?course=capstone&rating=10

# from flask import Flask, request
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     course = request.args["course"]  #gets the value associated with 'course' in the example url. 
#     rating = request.args.get("rating")  #gets the value assocaited with rating in the example url.
#     return {"message": f"{course} with rating {rating}"}

"""Dynamic Routes Examples"""

# # Static URL
# @app.route("/")
# def get_author():
#     response = requests.get('https://openlibrary.org/search/authors?q=Jane%20Austen')
#     if response.status_code == 200:
#         return response.content
#     elif response.status_code == 404:
#         return {"message": "Somthing went wrong!"}, 404
#     else:
#         return {"message": "Server error!"}, 500


# Parameterised example to get isbn for a book.
@app.route("/book/<isbn>") # the route requires a variable isbn
def get_author(isbn): # the variable isbn is expected to passed as an argument in the function
    res = requests.get("https://openlibrary.org/isbn/{escape(isbn)}.JSON") # the expected URL will have the value populated for the isbn.

    if res.status_code == 200:
        return {"message": res.JSON()}
    elif res.status_code == 404:
        return {"message": "Something went wrong!"}, 404

# # UUID example
# @app.route("/network/<uuid:uuid>")
# def uuid(uuid):
#     res = request.get("https://anotherapi/getnetwork/{uuid}.JSON")
#     if res.status_code == 200:
#         return {"message": res.JSON()}
#     elif res.status_code == 404:
#         return {"message": "Network not found"}
#     else:
#         return {"message": "Something went wrong"}
