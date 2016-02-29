from django.http import HttpResponse
from urllib.request import urlopen
from django.shortcuts import render
import urllib.request
import urllib.parse
import json

# make a GET request and parse the returned JSON
# note, no timeouts, error handling or all the other things needed to do this for real

def home(request):
    req = urllib.request.Request('http://exp-api:8000/recent_listings')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    
    return render(request, 'homepage.html', resp)


def listing(request, listing_id):
    req = urllib.request.Request('http://exp-api:8000/recent_listings')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return render(request, 'listing.html', resp)

