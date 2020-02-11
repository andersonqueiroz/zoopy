from zoopy.utils import get, put, post, delete, get_marketplace_id
from zoopy.models import marketplace


BASE_MODEL_URL = '/invoices'


def get_full_url():
    return BASE_MODEL_URL

def list(params={}, is_beta=False):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}'
    return get(url, params=params, is_beta=is_beta)

def list_by_seller(seller_id, params={}, is_beta=False):
    url = f'{marketplace.get_full_url()}/sellers/{seller_id}{BASE_MODEL_URL}'
    return get(url, params=params, is_beta=is_beta) 

def details(invoice_id, is_beta=False):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{invoice_id}'
    return get(url, is_beta=is_beta)

def create(params, is_beta=False):
    url = f'{marketplace.get_full_url()}{get_full_url()}'
    return post(end_point=url, data=params, is_beta=is_beta)

def approve(invoice_id, is_beta=False):
    url = f'{marketplace.get_full_url()}{get_full_url()}/{invoice_id}/approve'
    return post(end_point=url, is_beta=is_beta)

def void(invoice_id, is_beta=False):
    url = f'{marketplace.get_full_url()}{get_full_url()}/{invoice_id}/void'
    return delete(end_point=url, is_beta=is_beta) #Na documentação está POST mas a API só responde ao DELETE

def update(invoice_id, params, is_beta=False):
    url = f'{marketplace.get_full_url()}{get_full_url()}/{invoice_id}'
    return put(end_point=url, data=params, is_beta=is_beta)

def remove(invoice_id, is_beta=False):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{invoice_id}'
    return delete(url, is_beta=is_beta)
