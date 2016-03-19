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

def login(request):
    if 'username' in request.GET and 'password' in request.GET:
        username = request.GET['username']
        password = request.GET['password']
        url = 'http://models-api:8000/verify/?username=%s&password=%s' % (username, password)
        req = urllib.request.Request(url)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        # return HttpResponse()
    else:
        return HttpResponse("Something broke")
    # Get username and password
    
def create_user(request):
    if 'username' in request.GET and 'password' in request.GET:
        username = request.GET['username']
        password = request.GET['password']
        # API call to models
        url = 'http://models-api:8000/create_user/?username=%s&password=%s' % (username, password)
        req = urllib.request.Request(url)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        return HttpResponse(resp)
    else:
        return HttpResponse('something broke')
