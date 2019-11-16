import os
import pickle
from flask import Blueprint, Response
from actions.utilities import load_pickled_data
"""
These APIs will act as data pipelines to power the frontend UI
"""
interface = Blueprint('interface', __name__)


@interface.route('/locations', methods=['GET'])
def interface_locations():
    try:
        fp = os.path.join('store', 'interface.sav')
        obj = load_pickled_data(fp)
        res = ';'.join(obj['locationlist'])
        return Response(res, status=200)
    except:
        return Response('Server Error: Interface Modules Not Found', status=500)


@interface.route('/contexts', methods=['GET'])
def interface_contexts():
    try:
        fp = os.path.join('store', 'interface.sav')
        obj = load_pickled_data(fp)
        res = ';'.join(obj['contextlist'])
        return Response(res, status=200)
    except:
        return Response('Server Error', status=500)


@interface.route('/cuisines', methods=['GET'])
def interface_cuisines():
    try:
        fp = os.path.join('store', 'interface.sav')
        obj = load_pickled_data(fp)
        res = ';'.join(obj['cuisinelist'])
        return Response(res, status=200)
    except:
        return Response('Server Error', status=500)


@interface.route('/', methods=['GET'])
def interface_test_route():
    return "Hello, World!"
