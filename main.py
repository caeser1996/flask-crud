from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import redirect, url_for
from flask import request, jsonify

from app import app, mongo


# Create User
@app.route("/create", methods=['POST'])
def create_user():
    req_json = request.json
    #  name and email
    name = req_json["name"]
    email = req_json["email"]
    # save details of the user
    mongo.db.user.insert({'name': name, 'email': email})
    resp = jsonify("User created")
    resp.status_code = 200
    return resp


# Get Users
@app.route("/get-users")
def fetch_user():
    # if you want to select specific fields
    # users = mongo.db.user.find({}, {'name': 1, '_id': 0})
    users = mongo.db.user.find({}, {'name': 1, '_id': 1, 'email': 1})
    resp = dumps(users)
    return resp


# fetch a user with a id
@app.route("/get-user/<id>")
def get_user(id):
    user = mongo.db.user.find({'_id': ObjectId(id)})
    resp = dumps(user)
    return resp


# Edit User
@app.route("/update-user", methods=['PUT'])
def update_user():
    req_json = request.json
    #  name and email
    name = req_json["name"]
    id = req_json["_id"]
    email = req_json["email"]
    mongo.db.user.update_one({'_id': ObjectId(id)}, {'$set': {'name': name, 'email': email}})
    resp = jsonify("User Updated")
    resp.status_code = 200
    return resp


# Delete User
@app.route("/delete-user/<id>", methods=['DELETE'])
def delete_user(id):
    mongo.db.user.delete_one({'_id': ObjectId(id)})
    resp = jsonify("User Deleted")
    resp.status_code = 200
    return resp


@app.route('/', methods=['GET'])
def metrics():
    return redirect(url_for('static', filename='index.html'))


if __name__ == "__main__":
    app.run(debug=True)
