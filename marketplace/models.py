from django.db import models

class merchant(models.Model):
    username = models.CharField(max_length=11)
    publickey = models.TextField()
    bitcoin_credit = models.FloatField()
    
    
