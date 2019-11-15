from flask import Blueprint, request, Response
from actions.recommendations import get_restaurant_recommendations

recommendations = Blueprint('recommendations', __name__)


@recommendations.route('/restaurant', methods=['POST'])
def restaurant_recommendations():
    try:
        req = request.get_json()
        contexts = req.get("contexts")
        location = req.get("location")
        cuisines = req.get("cuisines")
        recommendations = get_restaurant_recommendations(contexts, location, cuisines)
        return Response(recommendations, status=200)
    except:
        return Response('Server Error', status=500)
