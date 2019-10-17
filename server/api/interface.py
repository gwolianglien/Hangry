from flask import Blueprint, request, Response
from actions.interface import get_all_unique_attributes

interface = Blueprint('interface', __name__, url_prefix='/api/interface')


@interface.route('/locations', methods=['GET'])
def all_locations():
    locations = get_all_unique_attributes(key='districts')
    return locations


@interface.route('/vibes', methods=['GET'])
def all_vibes():
    vibes = get_all_unique_attributes(key='contexts')
    return vibes


@interface.route('/cuisines', methods=['GET'])
def all_cuisines():
    cuisines = get_all_unique_attributes(key='cuisines')
    return cuisines
