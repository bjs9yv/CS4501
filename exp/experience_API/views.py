import urllib.request
import urllib.parse
import json
from django.http import HttpResponse

def listing_service(request):
    # call the API to return most recent listings

def recent_listings(request):
    req = urllib.request.Request('http://172.17.0.3/listing')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return HttpResponse(resp)
