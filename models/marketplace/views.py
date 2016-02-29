from rest_framework import viewsets
from .serializers import ListingSerializer, TransactionSerializer, MessageSerializer, MerchantSerializer
from .models import Listing, Merchant, Message, Transaction

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
