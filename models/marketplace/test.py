from django.test import TestCase
from django.test import Client
from .models import Merchant, Listing, Authenticator 
import json
import requests
import json

class MerchantTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Merchant.objects.create(username= "miller", password= "hunter2" )

    def tearDown(self):
        self.user.delete()

    def testNewMerchant(self):

        user = Merchant.objects.get(username="miller")
        self.assertTrue(user)
        


class ListingTests(TestCase):
    def setUp(self):
        self.client=Client()
        self.Listing1= Listing.objects.create(title= "ASDF", description="qwerty", bitcoin_cost= 45, quantity_available= 10)
        self.Listing2=Listing.objects.create(title= "Water Bottle", description="pink", bitcoin_cost= 3, quantity_available= 5) 
        
    def tearDown(self):
        self.Listing1.delete()
        self.Listing2.delete()
        
    def testNewListing(self):
        listing1=Listing.objects.get(title= "ASDF", description= "qwerty")
        listing2=Listing.objects.get(title="Water Bottle", description= "pink")
        self.assertTrue(listing1 != listing2)

    def testGetListingPath(self):

        response = self.client.get('listing/id/1/')
        self.assertTrue(response.status_code, 200)

    def testGetListingJson(self):
        response = self.client.get('listing/id/1/',{'title':'ASDF', 'description':'querty', 'bitcoin_cost': '45', 'quantity_available':'10'})

        self.assertTrue(response.status_code,200)



    
