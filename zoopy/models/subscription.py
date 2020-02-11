from zoopy.utils import get, put, post, delete, get_marketplace_id
from zoopy.models import marketplace


BASE_MODEL_URL = '/subscriptions'


def get_full_url():
    return BASE_MODEL_URL

def list(params={}, is_beta=False):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}'
    return get(url, params=params, is_beta=is_beta)

def list_by_seller(seller_id, params={}, is_beta=False):
    url = f'{marketplace.get_full_url()}/sellers/{seller_id}{BASE_MODEL_URL}'
    return get(url, params=params, is_beta=is_beta) 

def details(subscription_id, params={}, is_beta=False):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{subscription_id}'
    return get(url, params=params, is_beta=is_beta)

def create(params, is_beta=False):
    url = f'{marketplace.get_full_url()}{get_full_url()}'
    return post(end_point=url, data=params, is_beta=is_beta)

def suspend(subscription_id, is_beta=False):
    url = f'{marketplace.get_full_url()}{get_full_url()}/{subscription_id}/suspend'
    return post(end_point=url, is_beta=is_beta)

def reactivate(subscription_id, is_beta=False):
    url = f'{marketplace.get_full_url()}{get_full_url()}/{subscription_id}/reactivate'
    return post(end_point=url, is_beta=is_beta)

def update(subscription_id, params, is_beta=False):
    url = f'{marketplace.get_full_url()}{get_full_url()}/{subscription_id}'
    return put(end_point=url, data=params, is_beta=is_beta)

def remove(subscription_id, is_beta=False):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{subscription_id}'
    return delete(url, is_beta=is_beta)
