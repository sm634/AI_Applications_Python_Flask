from flask import Flask, make_response, request
from server_data import data
app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"

@app.route("/no_content/")
def no_content():
    return ({"message": "No content found"}, 200)

@app.route("/exp/")
def index_explicit():
    """return 'Hello World' message with a status code of 200
    Returns:
        string: Hello World
        status code: 200
    """
    response = make_response("Hello world!")
    response.status_code = 200
    return response

@app.route("/data/")
def get_data():
    length = len(data)
    try:
        if data and length > 0:
            return {"message": f"Data of length {length} found."}
        else:
            return {"message": "Data is empty"}, 500
    
    except:
        return {"message": "Data not found"}, 404

@app.route("/name_search")
def name_search():
    """find a person in the database
    Returns:
        json: person if found, with status of 200
        404: if not found
        422: if argument q is missing
    """
    query = request.args.get("q")
    print(query)

    if not query:
        return {"message": "Invalid input parameter"}, 422
    
    for person in data:
        if query.lower() in person["first_name"].lower():
            return person
        
    return ({"message": "Person not found"}, 404)

@app.route("/count", methods=["GET"])
def count():
    try:
        return {"data count": len(data)}, 200
    except NameError:
        return {"message": "data not defined"}, 500

@app.route("/person/<uuid>/")
def find_by_uuid(uuid):
    for person in data:
        if person["id"] == uuid:
            return person

    return {"message": "Person not found"}, 404

@app.route("/person/delete/<uuid>/")
def delete_by_uuid(uuid):
    for person in data:
        if person["id"] == str(uuid):
            data.remove(person)
            return {"message": f"{uuid}"}, 200
    
    return {"message": "Person not found"}, 404

@app.route('/person/create/', methods=["POST"])
def add_by_uuid():
    new_person = request.json
    print(new_person)
    if not new_person:
        return {"message": "Invalid input parameter"}, 422
    # code to validate new_person omitted
    try:
        data.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500
    
    return {"message": f"{new_person['id']}"}, 200

# Error handler
@app.errorhandler(404)
def api_not_found(error):
    return {"message": "API not found"}, 404
