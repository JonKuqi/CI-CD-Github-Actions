from flask import Flask, request, jsonify
from api.routes import recommender_blueprint
import os

app = Flask(__name__)
app.register_blueprint(recommender_blueprint)

@app.route("/", methods=['GET'])
def home():
    return jsonify({"message": "Recommender System API is running!"})


# branch Difference

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

