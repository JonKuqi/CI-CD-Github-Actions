from flask import Blueprint, request, jsonify
from core.main import MergingItemAndUserBased

recommender_blueprint = Blueprint("recommend", __name__)

@recommender_blueprint.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    userId = data.get("user_id")

    if not userId:
        return jsonify({"error": "Missing user_id"}), 400

    recomendations = MergingItemAndUserBased.mergeItemAndUserBased(userId)
    return jsonify({"recommendations": recomendations})
