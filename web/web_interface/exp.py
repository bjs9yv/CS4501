import requests
import json
from django.views.decorators.csrf import csrf_exempt

"""
These methods are API calls to the experience API layer
We pull these out to make the code more readable in views.py
"""

def recent_listings_exp_api():
    url = 'http://exp-api:8000/recent_listings'
    resp = requests.get(url).json()
    return resp

def create_account_exp_api(username, password):
    url = 'http://exp-api:8000/create_user/'
    url += '?username=%s&password=%s' % (username, password)
    resp = requests.get(url).json()
    return resp

def login_exp_api(username, password):
    url = 'http://exp-api:8000/login/'
    url += '?username=%s&password=%s' % (username, password)
    resp = requests.get(url).json()
    return resp

def logout_exp_api(auth):
    url = 'http://exp-api:8000/logout/'
    url += '?auth=%s' % (auth)
    resp = requests.get(url).json()
    return resp

@csrf_exempt
def create_listing_exp_api(title, description, bitcoin_cost, quantity_available):
    url = 'http://exp-api:8000/create_listing_service/?'
    postdata = {'title': title,
                'description': description,
                'bitcoin_cost': bitcoin_cost,
                'quantity_available': quantity_available}
    resp = requests.post(url, data=postdata)
    return resp

def search_exp_api(query):
    url = 'http://exp-api:8000/search_results_service/'
    url += '?query=%s' % (query)
    resp = requests.get(url).json()
    return resp

def add_to_cart_api(listing_id, auth):
    url = 'http://exp-api:8000/add_to_cart_service/'
    url += '?id=%s&auth=%s' % (listing_id, auth)
    resp = requests.get(url).json()
    return resp

def get_cart_service(auth):
    url = 'http://exp-api:8000/get_cart_service/'
    url += '?auth=%s' % (auth)
    resp = requests.get(url).json()
    return resp
