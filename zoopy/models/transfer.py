from zoopy.utils import get, put, post, delete
from zoopy.models import marketplace 

BASE_MODEL_URL = '/transfers'
BANK_ACCOUNTS_URL = '/bank_accounts/{0}/transfers'

def list_all():
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}'
    return get(url)

def details(transfer_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{transfer_id}'
    return get(url)

def transactions(transfer_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{transfer_id}/transactions'
    return get(url)

def create(bank_account_id, params):
    url = f'{marketplace.get_full_url()}{BANK_ACCOUNTS_URL.format(bank_account_id)}'
    return post(end_point=url, data=params)

def create_p2p(owner, receiver, params):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{owner}/to/{receiver}'
    return post(end_point=url, data=params)

def delete(transfer_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{transfer_id}'
    return delete(end_point=url, data=params)