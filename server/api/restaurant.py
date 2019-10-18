from flask import (
    Blueprint, request, Response
)

restaurant = Blueprint('restaurant', __name__)


@restaurant.route('/test', methods=['GET'])
def test_restaurant_route():
    return "Hello, Restaurant Route!"


@restaurant.route('/recommend', methods=['GET'])
def restaurant_recommendations():

    content = request.json
    contexts = content.get("contexts")
    location = content.get("location")


    return "Welcome to Hangry!"


@restaurant.route('/location', methods=['GET'])
def location_recommendations():
    return "Welcome to Hangry!"


@restaurant.route('/random', methods=['GET'])
def random_recommendations():
    return "Welcome to Hangry!"
