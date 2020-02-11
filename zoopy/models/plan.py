from zoopy.utils import get, put, post, delete, get_marketplace_id
from zoopy.models import marketplace


BASE_MODEL_URL = '/plans'


def get_full_url():
    return BASE_MODEL_URL

def list(params={}, is_beta=False):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}'
    return get(url, params=params, is_beta=is_beta)

def details(plan_id, is_beta=False):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{plan_id}'
    return get(url, is_beta=is_beta)

def create(params, is_beta=False):
    url = f'{marketplace.get_full_url()}{get_full_url()}'
    return post(end_point=url, data=params, is_beta=is_beta)

def update(plan_id, params, is_beta=False):
    url = f'{marketplace.get_full_url()}{get_full_url()}/{plan_id}'
    return put(end_point=url, data=params, is_beta=is_beta)

def remove(plan_id, is_beta=False):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{plan_id}'
    return delete(url, is_beta=is_beta)
