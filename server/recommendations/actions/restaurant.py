import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from interface import get_stored_data, get_unique_values


def get_restaurant_recommendations(location: str, contexts: list) -> list:
    if not location and not contexts:
        recommendations = random_recommendation()
    if not location and contexts:
        pass
    if location and not contexts:
        recommendations = location_recommendation(location)
    else:
        recommendations = full_recommendation(location, contexts)

    return recommendations


def random_recommendation() -> list:
    restaurantset = load_data()[0]
    restaurantset.sort(key=lambda restaurant: restaurant['rating'], reverse=True)  # sort by rating
    restaurantset = restaurantset[:25]  # filter to top 25 restaurants by rating
    recommendations = sample(restaurantset, 3)  # randomly pick 3 to recommend
    return recommendations


def location_recommendation(location: str) -> list:
    restaurantset = load_data()[0]

    relevant_restaurants = []
    for restaurant in restaurantset:

        # Check that user location is relevant to current restaurant
        locs = { loc for loc in restaurant['districtset'].split(';') }
        if location not in locs:
            continue
        relevant_restaurants.append(restaurant)

    relevant_restaurants.sort(key=lambda restaurant: restaurant['rating'], reverse=True)  # sort by rating
    relevant_restaurants = relevant_restaurants[:25]  # filter to top 25 restaurants by rating
    recommendations = sample(relevant_restaurants, 3)  # randomly pick 3 to recommend
    return recommendations


def context_recommendation(contexts: list) -> list:
    restaurantset, interface, metadata = load_data()
    contexts_map = { context: 0 for context in get_unique_values(interface['contextlist']) }

    # Get user vector
    temp = contexts_map.copy()
    for context in contexts:
        if context in contexts_map: temp[context] = 1
    user_context_vector = np.array(temp.values())

    relevant_restaurants = []
    for restaurant in restaurantset:

        # Compare and score restaurants
        temp = contexts_map.copy()
        for context in restaurant['contexts']:
            if context in curr_contexts: temp[context] = 1

        restaurant_context_vector = np.array(temp.values())
        cos_sim_score = cosine_similarity(user_context_vector, restaurant_context_vector)
        restaurant['score'] = cos_sim_score
        relevant_restaurants.append(restaurant)

    relevant_restaurants.sort(key=lambda x: x['score'], reverse=True)
    relevant_restaurants = relevant_restaurants[:25]
    recommendations = sample(relevant_restaurants, 3)  # randomly pick 3 to recommend
    return recommendations


def full_recommendation(location: str, contexts: list) -> list:

    restaurantset, interface, metadata = load_data()
    contexts_map = { context: 0 for context in get_unique_values(interface['contextlist']) }

    # Get user vector
    temp = contexts_map.copy()
    for context in contexts:
        if context in contexts_map: temp[context] = 1
    user_context_vector = np.array(temp.values())

    relevant_restaurants = []
    for restaurant in restaurantset:

        # Check that user location is relevant to current restaurant
        locs = { loc for loc in restaurant['districtset'].split(';') }
        if location not in locs:
            continue

        # Compare and score restaurants
        temp = contexts_map.copy()
        for context in restaurant['contexts']:
            if context in curr_contexts: temp[context] = 1

        restaurant_context_vector = np.array(temp.values())
        cos_sim_score = cosine_similarity(user_context_vector, restaurant_context_vector)
        restaurant['score'] = cos_sim_score
        relevant_restaurants.append(restaurant)

    relevant_restaurants.sort(key=lambda x: x['score'], reverse=True)
    relevant_restaurants = relevant_restaurants[:25]
    recommendations = sample(relevant_restaurants, 3)  # randomly pick 3 to recommend
    return recommendations


if __name__ == '__main__':
    get_restaurant_recommendations()
