from zoopy.utils import get, put, post, delete, get_marketplace_id
from zoopy.models import marketplace


BASE_MODEL_URL = '/sellers'
DOCUMENTS_URL = '/documents'
INDIVIDUALS_URL = f"{BASE_MODEL_URL}/individuals"
BUSINESSES_URL = f"{BASE_MODEL_URL}/businesses"
   

def get_full_url(seller_type):
    if seller_type == 'business':
        return BUSINESSES_URL
    return INDIVIDUALS_URL

def list():
    marketplace_id = get_marketplace_id()
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}'
    return get(url)

def details(seller_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{seller_id}'
    return get(url)

def create(params, seller_type):
    url = f'{marketplace.get_full_url()}{get_full_url(seller_type)}'
    return post(end_point=url, data=params)

def update(seller_id, seller_type, params):
    url = f'{marketplace.get_full_url()}{get_full_url(seller_type)}/{seller_id}'
    return put(end_point=url, data=params)

def remove(seller_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{seller_id}'
    return delete(url)

#Documentos
def add_documment(seller_id, params, files):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{seller_id}{DOCUMENTS_URL}'
    return post(end_point=url, data=params, files=files)

def update_document(document_id, params):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}{DOCUMENTS_URL}/{document_id}/'
    return put(end_point=url, data=params)

def get_documents(seller_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{seller_id}{DOCUMENTS_URL}'
    return get(url)

#Transferencias
def transfers(seller_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{seller_id}/transfers'
    return get(url)