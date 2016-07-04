from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
import requests
import json
from .forms import RegistrationForm, LoginForm, CreateListingForm
from .exp import *
from django.shortcuts import render_to_response


def cart(request):
    auth = request.COOKIES.get('auth')
    if not auth:
        # Currently you must be logged in to use the shopping cart, TODO is guest with cookies
        return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing"))
    if request.method == "GET":
        context = {'auth': auth}
        if 'id' in request.GET:
            resp = add_to_cart_api(request.GET['id'], auth) # TODO: this mean auth needs to be remade each time
            context['response'] = resp['response']
        # show the user their cart's items
        cart = get_cart_service(auth)
        context['items'] = cart['items']
        context['total'] = cart['total']
        return render(request, 'cart.html', context)
    return HttpResponseRedirect('home')

def search(request):
    auth = request.COOKIES.get('auth')
    if request.method == "GET":
        if 'query' in request.GET:
            query = request.GET['query']
            resp = search_exp_api(query)['hits']['hits']
            results = []
            for r in resp:
                results.append(r['_source'])
            context = {'results': results, 'auth': auth}
            return render(request, 'SRP.html', context)
    return HttpResponseRedirect('home')

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
        form = CreateListingForm()
        context = {'form': form, 'auth': auth}
        return render (request, 'create_listing.html', context )
    elif request.method == 'POST':
        form = CreateListingForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            bitcoin_cost = form.cleaned_data['bitcoin_cost']
            quantity_available = form.cleaned_data['quantity_available']
            resp = create_listing_exp_api(title, description, bitcoin_cost, quantity_available)
            if not resp or not '201':
                errors = 'Sorry please refresh and try again' 
                context = {'form': form, 'errors': errors, 'auth': auth}
                return render(request, 'create_listing.html', context)
            else:
                # redirect to success page
                return TemplateResponse(request, 'listing_success.html', {})
        else:
            form = CreateListing()
            context = {'form': form, 'auth': auth}
            return render (request, 'create_listing.html', context)
                
def listing(request, listing_id):
    url = 'http://exp-api:8000/listing_service/?listing_id='
    url += str(listing_id)
    resp = requests.get(url).json()
    return render(request, 'listing.html', resp)
