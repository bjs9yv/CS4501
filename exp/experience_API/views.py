import urllib.request
import urllib.parse
import json
from django.http import HttpResponse

def listing_service(request):
    pass
    # return a specific listing when a listing was clicked on

def recent_listings(request):
    req = urllib.request.Request('http://models-api:8000/listing')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    return HttpResponse(resp_json)
