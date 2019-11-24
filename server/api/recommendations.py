from flask import Blueprint, request, Response, jsonify
from actions.recommendations import get_restaurant_recommendations

recommendations = Blueprint('recommendations', __name__)


@recommendations.route('/restaurant', methods=['POST'])
def restaurant_recommendations():
    try:
        req = request.get_json()
        contexts = req.get("contexts")
        locations = req.get("locations")
        cuisines = req.get("cuisines")
        recommendations = get_restaurant_recommendations(contexts, locations, cuisines)

        recs = {}
        for i in range(len(recommendations)):
            name = 'rec{}'.format(i+1)
            recs[name] = recommendations[i]
        obj = jsonify(recs)

        return obj
    except:
        return Response('Server Error', status=500)
