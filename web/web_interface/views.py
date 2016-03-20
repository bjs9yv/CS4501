from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.hashers import make_password, check_password
from urllib.request import urlopen
import urllib.request
import urllib.parse
import json
from .forms import RegistrationForm, LoginForm

def login(request):
    if request.method == "GET":
        form = LoginForm()
        context = {'form': form}
        return render(request, 'loginpage.html', context)
    elif request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = make_password(form.cleaned_data['password'])
            # make API call to exp layer

@sensitive_post_parameters('username', 'password1', 'password2')
@csrf_protect
@never_cache
def create_account(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            password = make_password(password)
            # make API call to exp layer
            url = 'http://exp-api:8000/create_user/'
            url += '?username=%s&password=%s' % (username, password)
            req = urllib.request.Request(url)
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            resp = json.loads(resp_json)
            if 'create' in resp:
                if resp['create'] == True:
                    return HttpResponseRedirect(reverse('login'))
                elif resp['create'] == False:
                    context = {}
                    # TODO: failed to make account, username taken?
                    return render(request, 'create_account.html', context)
            return HttpResponse(resp)
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'create_account.html', context)

def home(request):
    url = 'http://exp-api:8000/recent_listings'
    req = urllib.request.Request(url)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)    
    return render(request, 'homepage.html', resp)


def listing(request, listing_id):
    url = 'http://exp-api:8000/listing_service/?listing_id='
    url += str(listing_id)
    req = urllib.request.Request(url)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return render(request, 'listing.html', resp)
