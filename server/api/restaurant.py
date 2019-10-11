from flask import (
    Blueprint, request, Response
)

restaurant = Blueprint('restaurant', __name__, url_prefix='/restaurant')

@restaurant.route('/', methods=['POST'])
def get_restaurants():
    return "Welcome to the Titanic Game!"

