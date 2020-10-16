import requests
import os

URL = ''
if os.path.exists('api_endpoint.txt'):
    with open('api_endpoint.txt') as f:
        URL = f.readline()

if 'FOTOPARADIES_API_URL' in os.environ:
    URL = os.environ['FOTOPARADIES_API_URL']

def get_order_info(shop, order):
    p = {'config':1320, 'shop': shop, 'order': order}
    if URL:
        r = requests.get(URL, params=p)
    else:
        raise Exception('No API endpoint', URL)
    return r.json()

def get_order_status(shop, order):
    return get_order_info(shop, order)['summaryStateCode']