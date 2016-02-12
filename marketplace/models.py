from django.db import models

class Merchant(models.Model):
    username = models.CharField(max_length=11)
    publickey = models.TextField()
    bitcoin_credit = models.FloatField()
    listing = models.ForeignKey(Listing)
    
    
class Listing (models.Model):
    title = models.TextField()
    description = models.TextField()
    bitcoin_cost = models.FloatField()

    quantity_available = models.FloatField()
