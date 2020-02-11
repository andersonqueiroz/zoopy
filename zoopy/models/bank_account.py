from zoopy.utils import get, put, post, delete, get_marketplace_id
from zoopy.models import marketplace

BASE_MODEL_URL = '/bank_accounts'

def get_full_url():
    return BASE_MODEL_URL

def list():
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}'
    return get(url)

def details(bank_account_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{bank_account_id}'
    return get(url)

def update(bank_account_id, params):
    url = f'{marketplace.get_full_url()}{get_full_url()}/{bank_account_id}'
    return put(end_point=url, data=params)

def remove(bank_account_id):
    url = f'{marketplace.get_full_url()}{get_full_url()}/{bank_account_id}'
    return delete(end_point=url)