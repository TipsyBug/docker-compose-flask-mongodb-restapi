from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

mongo_uri = "mongodb://mongo_db:27017/mydatabase"
client = MongoClient(mongo_uri)
db = client.mydatabase
collection = db.mycollection

@app.route("/items", methods=["POST"])
def create_item():
    data = request.json
    key = data.get("key")
    value = data.get("value")

    if key and value:
        collection.insert_one({"key": key, "value": value})
        return jsonify({"message": "Item created"}), 201
    else:
        return jsonify({"message": "Invalid data"}), 400

@app.route("/items/<key>", methods=["GET"])
def get_item(key):
    item = collection.find_one({"key": key})
    if item:
        return jsonify({"key": item["key"], "value": item["value"]}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

@app.route("/items/<key>", methods=["PUT"])
def update_item(key):
    data = request.json
    new_value = data.get("value")

    if new_value:
        result = collection.update_one({"key": key}, {"$set": {"value": new_value}})
        if result.matched_count > 0:
            return jsonify({"message": "Item updated"}), 200
        else:
            return jsonify({"message": "Item not found"}), 404
    else:
        return jsonify({"message": "Invalid data"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
