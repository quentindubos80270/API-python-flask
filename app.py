from flask import Flask, jsonify, request

app = Flask(__name__)

items = []

@app.route("/")
def home():
    return jsonify({"message": "Hello World!"})

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Invalid item"}), 400

    new_item = {
        "id": len(items) + 1,
        "name": data["name"]
    }

    items.append(new_item)
    return jsonify({"message": "Item added", "item": new_item}), 201

@app.route("/items", methods=["DELETE"])
def delete_items():
    items.clear()
    return jsonify({"message": "All items deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)