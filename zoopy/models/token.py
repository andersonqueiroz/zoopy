from zoopy.utils import get, put, post, delete, get_marketplace_id
from zoopy.models import marketplace

BASE_MODEL_URL = '/tokens'
BASE_MODEL_CARD_URL = '/cards'
BASE_MODEL_BANK_ACCOUNT_URL = '/bank_accounts'

def get_full_url(token_type):
    if token_type == 'bank_account':
        return f'{BASE_MODEL_BANK_ACCOUNT_URL}{BASE_MODEL_URL}'
    return f'{BASE_MODEL_CARD_URL}{BASE_MODEL_URL}'

def details(token_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{token_id}'
    return get(url)

def create(token_type, params):
    url = f'{marketplace.get_full_url()}{get_full_url(token_type)}'
    return post(end_point=url, data=params)

def attach_bank_account(token_id, customer_id):
    url =  f'{marketplace.get_full_url()}{BASE_MODEL_BANK_ACCOUNT_URL}'
    data = {'customer':customer_id, 'token':token_id}
    return post(end_point=url, data=data)

def attach_card(token_id, customer_id):
    url =  f'{marketplace.get_full_url()}{BASE_MODEL_CARD_URL}'
    data = {'customer':customer_id, 'token':token_id}
    return post(end_point=url, data=data)

def delete_bank_account(bank_account_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_BANK_ACCOUNT_URL}/{bank_account_id}'
    return delete(url)