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
def create_items():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Invalid item"}), 400

    items.append(data)
    return jsonify({"message": "Item added", "item": data}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)