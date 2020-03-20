from zoopy.utils import get, get_marketplace_id

MODEL_BASE_URL = '/marketplaces'


def get_full_url():
    return f'{MODEL_BASE_URL}/{get_marketplace_id()}'

def get_details(params):
    return get(get_full_url())