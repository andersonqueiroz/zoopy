import json
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'https://api.zoop.ws/v1'
BASE_URL_BETA = 'https://api-beta.zoop.ws/v2'

TOKEN = None
MARKETPLACE_ID = None

def get_base_url(is_beta=False):
    return BASE_URL_BETA if is_beta else BASE_URL

def validate_response(zoopy_response):
    if zoopy_response.status_code in [200, 201, 204, 304]:
        try:
            return zoopy_response.json()
        except:
            return zoopy_response
    else:
        return error(zoopy_response)


def get_marketplace_id():
    return MARKETPLACE_ID


def authentication_key(api_key=None, marketplace_id=None):
    global TOKEN    
    global MARKETPLACE_ID    
    TOKEN = HTTPBasicAuth(api_key, '')
    MARKETPLACE_ID = marketplace_id


def get(end_point, params = {}, is_beta=False):
    base_url = get_base_url(is_beta)
    url = f'{base_url}{end_point}'
    zoopy_response = requests.get(url, params=params, headers=headers(), auth=TOKEN)    
    return validate_response(zoopy_response)


def post(end_point, data = {}, files = {}, is_beta=False):
    base_url = get_base_url(is_beta)
    url = f'{base_url}{end_point}'
    if files:
        zoopy_response = requests.post(url, data=data, files=files, auth=TOKEN)
    else:
        zoopy_response = requests.post(url, json=data, headers=headers(), auth=TOKEN)
    return validate_response(zoopy_response)


def put(end_point, data = {}, files = {}, is_beta=False):
    base_url = get_base_url(is_beta)
    url = f'{base_url}{end_point}'
    if files:
        zoopy_response = requests.put(url, data=data, files=files, auth=TOKEN)
    else:        
        zoopy_response = requests.put(url, json=data, headers=headers(), auth=TOKEN)
    return validate_response(zoopy_response)


def delete(end_point, is_beta=False):
    base_url = get_base_url(is_beta)
    url = f'{base_url}{end_point}'
    zoopy_response = requests.delete(url, headers=headers(), auth=TOKEN)
    return validate_response(zoopy_response)

# def to_json(data):
#     if data:
#         dicionary = json.loads(json.dumps(data, default=lambda o: o.__dict__))
#         return json.dumps(dicionary)
#     return {}


def error(zoop_response):
    error_response = {
        "message":zoop_response.json() if zoop_response.content else 'Zoop API returned an error',
        "status_code": zoop_response.status_code,
    }
    raise Exception(error_response)


def headers():
    return {
        'accept': 'application/json',
    }
