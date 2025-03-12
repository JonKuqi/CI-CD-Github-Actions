from flask import Flask, request, jsonify
from api.routes import recommender_blueprint


app = Flask(__name__)
app.register_blueprint(recommender_blueprint)

@app.route("/", methods=['GET'])
def home():
    return jsonify({"message": "Recommender System API is running!"})

if __name__ == "__main__":
    app.run(debug=True)


