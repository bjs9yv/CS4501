import requests
from rest_framework import viewsets
from .serializers import ListingSerializer, TransactionSerializer, MessageSerializer, MerchantSerializer
from .models import Listing, Merchant, Message, Transaction, Authenticator, ShoppingCart
import os
import hmac
import json
import datetime
from django.contrib.auth.hashers import check_password, make_password
from django.conf import settings
from django.http import HttpResponse, JsonResponse

class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows listings to be viewed or edited.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def get(self, request, format=None):
        return Listing.objects.filter(id=request.GET['listing_id'])
         
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

def add_to_cart(request):
    if request.method != 'GET':
        return HttpResponse(json.dumps({'added': False, 'response': 'Bad request. Use GET'}))
    if 'id' in request.GET and 'auth' in request.GET:
        id = request.GET['id']
        if Listing.objects.filter(id=id):
            listing = Listing.objects.get(id=id)
            # Grab the user from the auth token
            if Authenticator.objects.filter(authenticator=request.GET['auth']):
                auth = Authenticator.objects.get(authenticator=request.GET['auth'])
                user = auth.userid
                cart = ShoppingCart.objects.get(account=user)
                cart.items.add(listing)
                return HttpResponse(json.dumps({'added': True, 'response': 'Listing added to cart'}))
            else:
                return HttpResponse(json.dumps({'added': False, 'response': 'Auth 404'}))
        else:
            return HttpResponse(json.dumps({'added': False, 'response': 'Listing 404'}))
    else:
            return HttpResponse(json.dumps({'added': False, 'response': 'Request missing id and/or auth'}))

def remove_from_cart(request):
    pass
    # cart.items.all() # all the items in the cart
    #cart.items.get(listing) # get just that item

def get_cart(request):
    pass
    # return relevant cart information on items, total, etc
        
def create_user(request):
    if request.method != 'GET':
        return HttpResponse(json.dumps({'create': False, 'response': 'Bad request. Use GET'}))
    if 'username' in request.GET and 'password' in request.GET:
        username = request.GET['username']
        password = request.GET['password']
        if Merchant.objects.filter(username=username):
            # check to see if username is already taken
            return HttpResponse(json.dumps({'create': False, 'response': 'Username taken'}))
        # Create the user with given username and password
        new_user = Merchant.objects.create()
        new_user.username = username
        # Store only salted hash of password with make_password()
        new_user.password = make_password(password)
        new_user.save()
        # Give the user a ShoppingCart
        cart = ShoppingCart(account=new_user)
        cart.save()
        return HttpResponse(json.dumps({'create': True, 'response': 'New User created'}))
    else:
        return HttpResponse(json.dumps({'create': False, 'response': 'Missing Username and/or password'}))

def verify_user(request):
    if request.method != 'GET':
        return HttpResponse(json.dumps({'ok': False, 'response': 'Bad HTTP request.'}))
    user = Merchant.objects.filter(username=request.GET['username'])
    if user.exists():
        user = Merchant.objects.get(username=request.GET['username'])
        if not check_password(request.GET['password'], user.password):
            # wrong password, but for security reasons we use a vaugue error message
            return HttpResponse(json.dumps({'ok':False, 'response': 'Incorrect username and/or pasword'}))
        datecreated = datetime.datetime.now()
        authenticator = hmac.new (key = settings.SECRET_KEY.encode('utf-8'), msg = os.urandom(32), digestmod = 'sha256').hexdigest()
        new_auth = Authenticator(userid=user, authenticator=authenticator, datecreated=datecreated)
        new_auth.save()
        # if by some miracle the authenticator is already in the DB, recreate it
        dup_auths = Authenticator.objects.filter(authenticator=authenticator)
        while len(dup_auths) != 1:
            for auth in dup_auths:
                auth.delete()
            authenticator = hmac.new (key = settings.SECRET_KEY.encode('utf-8'), msg = os.urandom(32), digestmod = 'sha256').hexdigest()
            new_auth = Authenticator(userid=user, authenticator=authenticator, datecreated=datecreated)
            new_auth.save()
        return HttpResponse(json.dumps({'ok':True, 'response':{'authenticator': new_auth.authenticator}}))
    else:
        return HttpResponse(json.dumps({'ok':False, 'response': 'Incorrect username and/or password '}))

def logout(request):
    if 'auth' in request.GET:
        auth = request.GET['auth']
        authenticator = Authenticator.objects.filter(authenticator=auth)
        if authenticator:
            authenticator = Authenticator.objects.get(authenticator=auth)
            authenticator.delete()
            return HttpResponse(json.dumps({'ok':True,'response':'Thank you, you are now logged out'}))
        return HttpResponse(json.dumps({'ok':True,'response':'Thats funny it looks like youre already logged out'}))
    else:
        resp = {'response':'it looks like you are already logged out'}
        resp_json = json.dumps(resp)
        return HttpResponse(resp_json)
