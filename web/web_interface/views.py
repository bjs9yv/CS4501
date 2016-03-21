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
    resp = recent_listings_exp_api()
    return render(request, 'homepage.html', resp)

def create_listing(request):
    auth = request.COOKIES.get('auth')
    if not auth:
      # handle user not logged in while trying to create a listing
      return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing"))
    
    
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
