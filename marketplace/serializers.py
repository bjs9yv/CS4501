from rest_framework import serializers
from models import Listing, Merchant, Message

class ListingSerializer(serializers.HyperlinedModelSerializer):
	class Meta:
		model = Listing
		fields = ('tite','description','bitcoin_cost','quantity_available')
