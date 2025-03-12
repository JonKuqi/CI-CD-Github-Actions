from flask import Flask, request, jesonify
from api.routes import recommender_blueprint


app = Flask(__name__)
app.register_blueprint(recommender_blueprint)


