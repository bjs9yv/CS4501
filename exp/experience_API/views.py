import requests
import urllib.request
import urllib.parse
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from kafka import KafkaProducer
from elasticsearch import Elasticsearch

def search_results_service(request):
    if 'query' in request.GET:
        query = request.GET['query']
        es = Elasticsearch(['es'])
        results = es.search(index='listing_index', body={'query': {'query_string': {'query': query}}, 'size': 10})
        return JsonResponse(results)

def add_to_cart_service(request):
    if 'id' in request.GET and 'auth' in request.GET:
        id = request.GET['id']
        auth = request.GET['auth']
        url = 'http://models-api:8000/add_to_cart/?auth=%s&id=%s' % (auth, id)
        resp = requests.get(url)
        # TODO: post to kafka
        return HttpResponse(resp)
    else:
        return HttpResponse(json.dumps({'added': 'false'}))

@csrf_exempt
def create_listing_service(request):
    if request.method == "POST":
        url = 'http://models-api:8000/listing/'
        postdata = {'title': request.POST['title'],
                    'description': request.POST['description'],
                    'bitcoin_cost': request.POST['bitcoin_cost'],
                    'quantity_available': request.POST['quantity_available']}
        r = requests.post(url, data=postdata)
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        producer.send('new-listings-topic', json.dumps(r.text).encode('utf-8'))
        return HttpResponse(r.status_code)
    else:
        return HttpResponse('400')

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
