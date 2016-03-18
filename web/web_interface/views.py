from django.http import HttpResponse
from urllib.request import urlopen
from django.shortcuts import render
import urllib.request
import urllib.parse
import json

def login(request):
    pass

def create_account(request):
    pass

def home(request):
    req = urllib.request.Request('http://exp-api:8000/recent_listings')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)    
    return render(request, 'homepage.html', resp)


def listing(request, listing_id):
    url = 'http://exp-api:8000/listing_service/?listing_id='
    url += str(listing_id)
    req = urllib.request.Request(url)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return render(request, 'listing.html', resp)

