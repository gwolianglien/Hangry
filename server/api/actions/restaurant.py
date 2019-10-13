import pandas as pd
import numpy as np
from interface import load_data


def get_restaurant_recommendations():
    pass



def get_location_recommendations():
    pass


def get_random_recommendations():
    pass


def get_unique_values(series: object):
    """
    :type series: Pandas Series
    :rtype: dict
    """
    uniques = list(set(series))
    uniques.sort()
    return { key:0 for key in uniques }


def cosine_similarity(vec1: list, vec2: list) -> float:
    numerator = np.dot(vec1, vec2)
    vec1_magnitude = np.linalg.norm(vec1)
    vec2_magnitude = np.linalg.norm(vec2)
    return numerator / (vec1_magnitude * vec2_magnitude)


def filter_restaurants_by_score(df, min_score=75):
    pass
