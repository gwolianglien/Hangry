import os
import pickle
from flask import Blueprint, Response
from api.actions.interface import get_interface_attributes

interface = Blueprint('interface', __name__)

@interface.route('/test', methods=['GET'])
def interface_test_route():
    return "Hello, Interface Route!"


@interface.route('/locations', methods=['GET'])
def interface_locations_list():
    try:
        path = os.path.join('api', 'data', 'interface.sav')
        raw_data = get_interface_attributes(path=path)
        locationslist = raw_data['locationlist']
        locationslist = ';'.join(locationslist)
        res = Response(locationslist, status=200)
        return res
    except FileNotFoundError:
        res = Response('Server Error: Interface Modules Not Found', status=500)
        return res


@interface.route('/contexts', methods=['GET'])
def interface_contexts_list():
    try:
        path = os.path.join('api', 'data', 'interface.sav')
        raw_data = get_interface_attributes(path=path)
        locationslist = raw_data['contextlist']
        locationslist = ';'.join(locationslist)
        res = Response(locationslist, status=200)
        return res
    except FileNotFoundError:
        res = Response('Server Error: Interface Modules Not Found', status=500)
        return res


@interface.route('/cuisines', methods=['GET'])
def all_cuisines():
    try:
        path = os.path.join('api', 'data', 'interface.sav')
        raw_data = get_interface_attributes(path=path)
        locationslist = raw_data['cuisinelist']
        locationslist = ';'.join(locationslist)
        res = Response(locationslist, status=200)
        return res
    except FileNotFoundError:
        res = Response('Server Error: Interface Modules Not Found', status=500)
        return res
