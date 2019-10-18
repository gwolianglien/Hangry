from flask import (
    Blueprint
)

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET'])
def test_route():
    return "Hello, World!"
