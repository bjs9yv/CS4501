from rest_framework import serializers
from .models import Listing, Merchant, Message, Transaction

class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = ('title','description','bitcoin_cost','quantity_available')
        
class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('product','quantity', 'buyer', 'seller', 'today', 'shipped_date','received_date', 'cancelled_date', 'failed_date', 'status')
        
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('sender','recipient','body','opened')
        
class MerchantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Merchant
        fields = ('username','publickey','bitcoin_credit','accounts', 'rating', 'is_seller', 'purchases')
        
