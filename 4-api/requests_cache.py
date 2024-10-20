import pickle

def load_cache(pickle_file):
    try:
        with open(pickle_file, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}
    
def clear_cache(pickle_file):
    with open(pickle_file, 'wb') as f:
        pickle.dump({}, f)
        return {}

def save_cache(cache, pickle_file):
    with open(pickle_file, 'wb') as f:
        pickle.dump(cache, f)

if __name__ == '__main__':
    cache = clear_cache('test.pkl')
    assert cache == {}
    cache['test'] = 'test'
    save_cache(cache, 'test.pkl')
    cache = load_cache('test.pkl')
    assert cache == {'test': 'test'}
    assert cache['test'] == 'test'

