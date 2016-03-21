from rest_framework import viewsets
from .serializers import ListingSerializer, TransactionSerializer, MessageSerializer, MerchantSerializer
from .models import Listing, Merchant, Message, Transaction, Authenticator
import os
import hmac

from django.conf import settings

import json
import datetime
from django.http import HttpResponse

class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows listings to be viewed or edited.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    # doesnt do anythong/ dont know how to make it work
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


def create_user(request):
    if request.method != 'GET':
        return HttpResponse(json.dumps({'create': False, 'response': 'Bad request. Use GET'}))

    if 'username' in request.GET and 'password' in request.GET:
        username = request.GET['username']
        password = request.GET['password']
        if Merchant.objects.filter(username=username):
            # check to see if username is already taken
            return HttpResponse(json.dumps({'create': False, 'response': 'Username taken'}))
        new_user = Merchant.objects.create()
        new_user.username = username
        new_user.password = password
        new_user.save()
        return HttpResponse(json.dumps({'create': True, 'response': 'New User created'}))
    else:
        return HttpResponse(json.dumps({'create': False, 'response': 'Missing Username and/or password'}))

def verify_user(request):
    if request.method != 'GET':
        return HttpResponse(json.dumps({'verify': False, 'response': 'Wrong HTTP request.'}))
    user = Merchant.objects.filter(username=request.GET['username'], password = request.GET['password'])
    if user.exists():
        return HttpResponse(user)
        datecreated = datetime.datetime.now() 
        authenticator = hmac.new (key = settings.SECRET_KEY.encode('utf-8'), msg = os.urandom(32), digestmod = 'sha256').hexdigest()
        userid = user.id()
        new_auth = Authenticator(userid=userid, authenticator=authenticator, datecreated=datecreated)
        new_auth.save()
        return HttpResponse(json.dumps({'verify':True, 'authenticator': new_auth.authenticator}))
    else:
        return HttpResponse(json.dumps({'verify':False, 'response': 'incorrect user.invalid credentials'}))
