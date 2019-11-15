import os
import pickle
from flask import Blueprint, Response
from actions.utilities import load_pickled_data
"""
These APIs will act as data pipelines to power the frontend UI
"""
interface = Blueprint('interface', __name__)


@interface.route('/locations', methods=['POST'])
def interface_locations():
    try:
        interface_fp = os.path.join('store', 'interface.sav')
        interface = load_pickled_data(interface_fp)
        locations = { locations: interface['locationlist'] }
        return Response(locations, status=200)
    except:
        return Response('Server Error: Interface Modules Not Found', status=500)


@interface.route('/contexts', methods=['POST'])
def interface_contexts():
    try:
        interface_fp = os.path.join('store', 'interface.sav')
        interface = load_pickled_data(interface_fp)
        contexts = { contexts: interface['contextlist'] }
        return Response(contexts, status=200)
    except:
        return Response('Server Error', status=500)


@interface.route('/cuisines', methods=['POST'])
def interface_cuisines():
    try:
        interface_fp = os.path.join('store', 'interface.sav')
        interface = load_pickled_data(interface_fp)
        cuisines = { cuisines: interface['cuisinelist'] }
        return Response(cuisines, status=200)
    except:
        return Response('Server Error', status=500)


@interface.route('/', methods=['GET'])
def interface_test_route():
    return "Hello, World!"
