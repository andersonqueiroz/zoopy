from zoopy.utils import get, put, post, delete
from zoopy.models import marketplace 

BASE_MODEL_URL = '/transactions'

def get_full_url():
    return BASE_MODEL_URL

def list(params={}):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}'
    return get(url, params=params)

def details(transaction_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{transaction_id}'
    return get(url)

def create(params):
    url = f'{marketplace.get_full_url()}{(get_full_url())}'
    return post(end_point=url, data=params)

def update(transaction_id, params):
    url = f'{marketplace.get_full_url()}{get_full_url()}/{transaction_id}'
    return put(end_point=url, data=params)

def void(transaction_id, params):
    url = f'{marketplace.get_full_url()}{get_full_url()}/{transaction_id}/void'
    return post(end_point=url, data=params)
