import os
import pickle
from flask import Blueprint, Response
from interface.actions.interface import load_data

interface = Blueprint('interface', __name__)


@interface.route('/locations', methods=['GET'])
def interface_locations_list():
    try:
        raw_data = load_data()[1]
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
        raw_data = load_data()[1]
        contextlist = raw_data['contextlist']
        contextlist = ';'.join(contextlist)
        res = Response(contextlist, status=200)
        return res
    except FileNotFoundError:
        res = Response('Server Error: Interface Modules Not Found', status=500)
        return res


@interface.route('/cuisines', methods=['GET'])
def interface_cuisines_list():
    try:
        raw_data = load_data()[1]
        cuisinelist = raw_data['cuisinelist']
        cuisinelist = ';'.join(cuisinelist)
        res = Response(cuisinelist, status=200)
        return res
    except FileNotFoundError:
        res = Response('Server Error: Interface Modules Not Found', status=500)
        return res
