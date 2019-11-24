import os
from random import sample
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from . utilities import load_restaurantset, load_interface


def get_restaurant_recommendations(contexts: list, locations: list, cuisines: list) -> list:
    if not contexts and not locations and not cuisines:
        return naive_recommendation()
    if locations and not contexts and not cuisines:
        return location_recommendation(locations=locations)
    if contexts and not locations and not cuisines:
        return context_recommendation(contexts=contexts)
    if contexts and locations and not cuisines:
        return context_location_recommendation(contexts=contexts, locations=locations)
    else:
        return []


"""
Recommendation Functions
"""
# Recommend based on no user input
def naive_recommendation() -> list:  # works
    restaurantset = load_restaurantset()
    recs = get_recommendations(restaurantset, random=True, top=15, num=3)
    return recs


# Recommend based on only a location input
def location_recommendation(locations: list) -> list:
    restaurantset = load_restaurantset()
    relevant_restaurants = location_filter(restaurantset, locations)
    recs = get_recommendations(relevant_restaurants)
    return recs


# Recommend based on only context inputs
def context_recommendation(contexts: list) -> list:
    restaurantset = load_restaurantset()
    relevant_restaurants = context_filter(restaurantset, contexts)
    recs = get_recommendations(relevant_restaurants)
    return recs


# Recommend based on context and location inputs
def context_location_recommendation(contexts: list, locations: list) -> list:
    restaurantset = load_restaurantset()
    relevant_restaurants = location_filter(restaurantset, locations)
    relevant_restaurants = context_filter(relevant_restaurants, contexts)
    recs = get_recommendations(relevant_restaurants)
    return recs


"""
Select a number of restaurants to recommend from a final list of relevant restaurants
"""
def get_recommendations(restaurantset, random=True, top=25, num=3) -> list:
    restaurantset.sort(key=lambda r: r['rating'], reverse=True)  # sort by rating
    restaurantset = restaurantset[:top]  # pick out top 25
    if random:
        recommendations = sample(restaurantset, num)  # choose 3 random from top 25
    else:
        recommendations = restaurantset[:num]
    return recommendations

"""
Filter functions to select relevant restaurants based on user inputs and criteria
"""
# Filter and select restaurants that contain the user location input
def location_filter(restaurantset: list, locations: list) -> list:
    locations = set(locations)
    relevant_restaurants = []
    for r in restaurantset:
        curr = r['districtset']
        for district in curr:
            if district in locations:
                relevant_restaurants.append(restaurantset)
                break
    return relevant_restaurants


# Filter and select restaurants that contain the user cuisines input
def cuisine_filter(restaurantset: list, cuisines: list) -> list:
    cuisines = set(cuisines)
    relevant_restaurants = []
    for r in restaurantset:
        curr_restaurant_cuisines = r['cuisinelist']  # curr restaurant cuisines
        for c in curr_restaurant_cuisines:
            if c in cuisines:
                relevant_restaurants.append(r)
                break
    return relevant_restaurants


# Filter and select restaurants that contain the user contexts input
def context_filter(restaurantset: list, contexts: list, top=50) -> list:
    contextlist = load_interface()['contextlist']
    contexts_map = { c: 0 for c in contextlist }

    # Get user map and vector
    user_map = contexts_map.copy()
    for c in contexts:
        if c in user_map: user_map[c] = 1
    user_arr = [ (context, user[context]) for context in user ]
    user_arr.sort(key=lambda x: x[0])  # sort by context in alphabetical order
    user_vector = [ x[1] for x in user_arr ]  # keep only the binary values

    # Compare and score restaurant context similarity
    for restaurant in restaurantset:
        curr = contexts_map.copy()
        for c in restaurant.get('contexts'):
            if context in curr_contexts: curr[c] = 1
        curr = [ (context, user[context]) for context in user ]
        curr.sort(key=lambda x: x[0])  # sort by context in alphabetical order
        curr = [ x[1] for x in curr ]
        cos_sim = cosine_similarity(user_vector, curr)
        restaurant['score'] = cos_sim

    restaurantset.sort(key=lambda r: r['score'], reverse=True)
    relevant_restaurants = restaurantset[:top]
    return relevant_restaurants
