import urllib.request
import urllib.parse
import json
from django.http import HttpResponse

def listing_service(request):
    if 'listing_id' in request.GET:
        url = 'http://models-api:8000/listing/'
        url += request.GET['listing_id']
        req = urllib.request.Request(url)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        return HttpResponse(resp_json)
    else:
        return HttpResponse('something broke')

def recent_listings(request):
    req = urllib.request.Request('http://models-api:8000/listing')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    return HttpResponse(resp_json)
