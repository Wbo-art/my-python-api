from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from your Python API on Choreo!"})

@app.route("/add", methods=["GET"])
def add_numbers():
    try:
        x = float(request.args.get("x", 0))
        y = float(request.args.get("y", 0))
        return jsonify({"result": x + y})
    except:
        return jsonify({"error": "Invalid input"}), 400

@app.route("/greet", methods=["POST"])
def greet():
    data = request.get_json()
    name = data.get("name", "friend")
    return jsonify({"message": f"Hello, {name}!"})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
