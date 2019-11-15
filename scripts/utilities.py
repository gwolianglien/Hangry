import os
import pickle


def load_pickled_file(filepath):
    try:
        f = open(filepath, 'rb')
        obj = pickle.load(f)
        return obj
    except FileNotFoundError:
        raise Exception('{} could not be found'.format(filepath))
    except:
        raise Exception('Error loading pickled file')


def store_pickled_file(obj, path, name):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        f = open(os.path.join(path, name), 'wb')
        pickle.dump(obj, f)
        f.close()
    except:
        raise Exception('Error storing object in {}'.format(name))
