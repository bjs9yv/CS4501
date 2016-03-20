from rest_framework import viewsets
from .serializers import ListingSerializer, TransactionSerializer, MessageSerializer, MerchantSerializer
from .models import Listing, Merchant, Message, Transaction
import os
import hmac
from .settings import SECRET_KEY
import json
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
        return HttpResponse(json.dumps({'create': False, 'Response': 'Bad request. Use GET'}))

    if 'username' in request.GET and 'password' in request.GET:
        # TODO: check to see if username is taken
        new_user = Merchant.objects.create()
        new_user.username = request.GET['username']
        new_user.password = request.GET['password']
        new_user.save()
        return HttpResponse(json.dumps({'create': True, 'response': 'New User created'}))

    else:
        return HttpResponse(json.dumps({'create': False, 'response': 'Missing Username and/or password'}))

def verify_user(response):
    user = Merchants.objects.filter(username=request.GET['username'], password = request.GET['password'])
    authenticator = None
    if user.exists():
        authenticator = hmac.new (key = settings.SECRET_KEY.encode('utf-8'), msg = os.urandom(32), digestmod = 'sha256').hexdigest()
    return HttpResponse(json.dumps({'authenticator': authenticator}))

    
            

