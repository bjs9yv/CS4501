from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from urllib.request import urlopen
import base64
import urllib.request
import urllib.parse
import json
from .forms import RegistrationForm, LoginForm

@sensitive_post_parameters('username', 'password')
@csrf_protect
@never_cache
def login(request):
    if request.method == "GET":
        next = request.GET.get('next') or reverse('home')
        form = LoginForm()
        context = {'form': form}
        return render(request, 'loginpage.html', context)
    elif request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            next = form.cleaned_data.get('next') or reverse('home')
            resp = login_exp_api(username, password)
            if not resp or not resp['ok']:
                # couldnt log them in, send back to login page with error
                errors = resp['response']
                context = {'form': form, 'errors': errors}
                return render(request, 'loginpage.html', context)
            # logged in, set login cookie and redirect to wherever they came from
            authenticator = resp['response']['authenticator']
            response = HttpResponseRedirect(next)
            response.set_cookie("auth", authenticator)
            return response
    else:
        form = LoginForm()
        context = {'form': form}
        return render(request, 'loginpage.html', context)

def logout(request):
    auth = request.COOKIES.get('auth')
    resp = logout_exp_api(auth)
    context = {'response': resp}
    response = TemplateResponse(request,'logout.html', context)
    response.delete_cookie('auth')
    return response

@sensitive_post_parameters('username', 'password1', 'password2')
@csrf_protect
@never_cache
def create_account(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            password = password
            # make API call to exp layer
            resp = create_account_exp_api(username, password)
            if 'create' in resp:
                if resp['create']:
                    return HttpResponseRedirect(reverse('login'))
                else:
                    # failed to make account, report error
                    errors = resp['response']
                    context = {'form': form, 'errors': errors}
                    return render(request, 'create_account.html', context)
            return HttpResponse(resp)
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'create_account.html', context)

def home(request):
    results = recent_listings_exp_api()
    auth = request.COOKIES.get('auth')
    context = {'results':results['results'], 'auth': auth}
    return render(request, 'homepage.html', context)

def create_listing(request):
    auth = request.COOKIES.get('auth')
    if not auth:
      # handle user not logged in while trying to create a listing
        return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing"))
    if request.method == 'GET':
        form = CreateListing()
        context = {'form': form}
        return render (request, 'create_listing.html', context )
    elif request.method == 'POST':
        form = CreateListing(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            bitcoin_cost = form.cleaned_data['bitcoin_cost']
            quantity_available = form.cleaned_data['quantity_available']

            resp = create_listing_exp_api(title, description, bitcoin_cost, quantity_available)

            if not resp or not resp['ok']:
                errors = resp['response']
                context = {'form': form, 'errors': errors}
                return render(request, 'create_listing.html', context)
        else:
            form = CreateListing()
            context = {'form': form}
            return render (request, 'create_listing.html', context)
                
def listing(request, listing_id):
    url = 'http://exp-api:8000/listing_service/?listing_id='
    url += str(listing_id)
    req = urllib.request.Request(url)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return render(request, 'listing.html', resp)

def recent_listings_exp_api():
    url = 'http://exp-api:8000/recent_listings'
    req = urllib.request.Request(url)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)    
    return resp

def create_account_exp_api(username, password):
    url = 'http://exp-api:8000/create_user/'
    url += '?username=%s&password=%s' % (username, password)
    req = urllib.request.Request(url)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return resp

def login_exp_api(username, password):
    url = 'http://exp-api:8000/login/'
    url += '?username=%s&password=%s' % (username, password)
    req = urllib.request.Request(url)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return resp

def logout_exp_api(auth):
    url = 'http://exp-api:8000/logout/'
    url += '?auth=%s' % (auth)
    req = urllib.request.Request(url)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return resp

<<<<<<< HEAD
def create_listing_exp_api():
    pass
=======
<<<<<<< HEAD
def create_listing_exp_api(title, description, bitcoin_cost, quantity_available):
    url = 'http://exp-api:8000/create_listing/'
    url += '?title=%s' % (title)
    url += '?description=%s' % (description)
#    url += '?bitcoin_cost=%s' % (bitcoin_cost)
#    url += '?quantity_available=%s' % (quantity_available)
=======
def create_listing_exp_api():
    pass
    
>>>>>>> f30411a08d2342c3ef7eca607c4fe54a4f13c235
>>>>>>> 4cc36e97e4a1347c7ab5366330feccee778ca6df
