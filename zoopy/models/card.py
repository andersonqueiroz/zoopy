from zoopy.utils import get, put, post, delete, get_marketplace_id
from zoopy.models import marketplace


BASE_MODEL_URL = '/cards'


def get_full_url():
    return BASE_MODEL_URL

def details(card_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{card_id}'
    return get(url)

def attach(params):
    url = f'{marketplace.get_full_url()}{get_full_url()}'
    return post(end_point=url, data=params)

def update(card_id, params):
    url = f'{marketplace.get_full_url()}{get_full_url()}/{card_id}'
    return put(end_point=url, data=params)

def remove(card_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{card_id}'
    return delete(url)