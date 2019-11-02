from flask import (
    Blueprint, request, Response
)
from api.actions.restaurant import (
    get_restaurant_recommendations
)

restaurant = Blueprint('restaurant', __name__)


@restaurant.route('/test', methods=['GET'])
def test_restaurant_route():
    return "Hello, Restaurant Route!"


@restaurant.route('/restaurant', methods=['GET'])
def restaurant_recommendations():
    try:
        content = request.json
        contexts = content.get("contexts")
        location = content.get("location")
        recommendations = get_restaurant_recommendations(location, contexts)
        res = Response(recommendations, status=200)
        return res
    except FileNotFoundError:
        res = Response('Server Error: Recommendation Engine Crashed!', status=500)
        return res
