import pandas as pd


def get_all_unique_attributes(key='districts', delimiter=';', sort=True) -> list:

    df = load_data()

    # handle if input cannot be found
    if key not in df:
        raise Exception('Metadata key could not be found')

    attributes = list(df[key])
    unique_attributes = []

    for attribute in attributes:
        arr = attribute.split(delimiter)
        unique_attributes.extend(arr)

    unique_attributes = list(set(unique_attributes))

    if sort is True:
        unique_attributes.sort()

    return unique_attributes


def load_data(file='metadata.csv', path='../../data/') -> object:
    try:
        df = pd.read_csv(path+file, keep_default_na=False)
        return df
    except:
        raise Exception('Error loading file')
