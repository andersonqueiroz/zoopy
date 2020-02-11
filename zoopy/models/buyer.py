from zoopy.utils import get, put, post, delete, get_marketplace_id
from zoopy.models import marketplace


BASE_MODEL_URL = '/buyers'


def get_full_url():
    return BASE_MODEL_URL

def list(params={}):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}'
    return get(url, params=params)

def details(buyer_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{buyer_id}'
    return get(url)

def create(params):
    url = f'{marketplace.get_full_url()}{get_full_url()}'
    return post(end_point=url, data=params)

def update(buyer_id, params):
    url = f'{marketplace.get_full_url()}{get_full_url()}/{buyer_id}'
    return put(end_point=url, data=params)

def remove(buyer_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{buyer_id}'
    return delete(url)
