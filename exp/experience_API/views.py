import requests
import urllib.request
import urllib.parse
import json
from django.http import HttpResponse

def create_listing_service(request):
    if 'data' in request.POST:
        url = 'http://models-api:8000/listing/'
        postdata = request.POST['data']
        r = requests.post(url, data=postdata)
        return HttpResponse(r)
    else:
        # return bad http post error code
        return HttpResponse(400) 

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

def logout(request):
    if 'auth' in request.GET:
        auth = request.GET['auth']
        url = 'http://models-api:8000/logout/?auth=%s' % (auth)
        req = urllib.request.Request(url)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        return HttpResponse(resp_json)
    else:
        resp = {'response':'it looks like you are already logged out'}
        resp_json = json.dumps(resp)
        return HttpResponse(resp_json)

def login(request):
    if 'username' in request.GET and 'password' in request.GET:
        username = request.GET['username']
        password = request.GET['password']
        url = 'http://models-api:8000/verify_user/?username=%s&password=%s' % (username, password)
        req = urllib.request.Request(url)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        return HttpResponse(resp_json)
    else:
        return HttpResponse("Something broke")
    
def create_user(request):
    if 'username' in request.GET and 'password' in request.GET:
        username = request.GET['username']
        password = request.GET['password']
        # API call to models
        url = 'http://models-api:8000/create_user/?username=%s&password=%s' % (username, password)
        req = urllib.request.Request(url)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        return HttpResponse(resp_json)
    else:
        return HttpResponse(json.dumps({'response':'something broke'}))
