from django.http import HttpResponse
from django.shortcuts import render
import urllib.request
import urllib.parse
import json


def home(request):
    req = urllib.request.Request('http://exp-api:8000/recent_listings')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return render(request, 'homepage.html', resp)
