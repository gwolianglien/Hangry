from flask import (
    Blueprint, request, Response
)

restaurant = Blueprint('restaurant', __name__, url_prefix='/api/restaurant')

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
