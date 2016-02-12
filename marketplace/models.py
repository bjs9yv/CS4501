from django.db import models

class Merchant(models.Model):
    username = models.CharField(max_length=11)
    publickey = models.TextField()
    bitcoin_credit = models.FloatField()
    accounts = models.TextField()
    rating = models.IntegerField(default=0)
    is_seller = models.BooleanField(default=False)
    purchases = models.ForeignKey(Listing)
    products = models.ForeignKey(Listing)
    
class Message(models.Model):
    sender = models.ForeignKey(Merchant, related_name='message_sender')
    recipient = models.ForeignKey(Merchant, related_name='message_recipient')
    body = models.TextField()
    opened = models.BooleanField(default=False)
    
class Listing (models.Model):
    title = models.TextField()
    description = models.TextField()
    bitcoin_cost = models.FloatField()
    quantity_available = models.FloatField()
