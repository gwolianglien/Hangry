import os
import pickle
import pandas as pd


def get_interface_attributes(path):
    file = open(path, 'rb')
    unpickled = pickle.load(file)
    return unpickled
