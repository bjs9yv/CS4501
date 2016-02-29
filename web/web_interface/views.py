from django.http import HttpResponse
from urllib.request import urlopen
from django.shortcuts import render
import urllib.request
import urllib.parse
import json

# make a GET request and parse the returned JSON
# note, no timeouts, error handling or all the other things needed to do this for real

def detail(request, listing_id):
        return HttpResponse("You're looking at listing %s." % listing_id)

def results(request, listing_id):
        response = "You're looking at the results of listing %s."
        return HttpResponse(listing_id)


def home(request):
    req = urllib.request.Request('http://172.17.0.4:8000/recent_listings')
    #req = urllib.request.Request('http://172.17.0.3:8000/')
    
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)    
    
    
    return render(request, 'homepage.html', resp)
