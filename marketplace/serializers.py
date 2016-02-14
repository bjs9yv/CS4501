from rest_framework import serializers
from models import Listing, Merchant, Message

class ListingSerializer(serializers.HyperlinedModelSerializer):
    class Meta:
        model = Listing
        fields = ('title','description','bitcoin_cost','quantity_available')
        
class TransactionSerializer(serializers.HyperlinedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('product','quantity', 'buyer', 'seller', 'today', 'shipped_date','received_date', 'cancelled date', 'failed_date', 'status')
        
class MessageSerializer(serializers.HyperlinedModelSerializer):
    class Meta:
        model = Message
        fields = ('sender','recipient','body','opened')
        
class MerchantSerializer(serializers.HyperlinedModelSerializer):
    class Meta:
        model = Merchant
        fields = ('username','publickey','bitcoin_credit','accounts', 'rating', 'is_seller', 'purchases')
        
