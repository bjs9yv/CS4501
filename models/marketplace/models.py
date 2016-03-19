from django.db import models
from django.utils import timezone
import datetime

class Listing (models.Model):
    title = models.TextField()
    description = models.TextField()
    bitcoin_cost = models.FloatField()
    quantity_available = models.FloatField()

class Merchant(models.Model):
    username = models.CharField(max_length=11)
    password = models.CharField(default='legacy migrations', max_length=512)
    
    publickey = models.TextField(blank=True)
    bitcoin_credit = models.FloatField(default=0)
    accounts = models.TextField(blank=True)
    rating = models.IntegerField(default=0)
    is_seller = models.BooleanField(default=False)
    purchases = models.ForeignKey(Listing, blank=True, null=True)
    
class Message(models.Model):
    sender = models.ForeignKey(Merchant, related_name='message_sender')
    recipient = models.ForeignKey(Merchant, related_name='message_recipient')
    body = models.TextField()
    opened = models.BooleanField(default=False)
    
class Transaction(models.Model):
    product = models.CharField(max_length=30)
    quantity = models.IntegerField()
    buyer = models.CharField(max_length=11)
    seller = models.CharField(max_length=11)
    # Assume two users in a transaction
    # 0. No transaction
    # 1. Seller shipped, merchant has not received (incomplete)
    # 2. Seller shipped, merchant has received (complete)
    # 3. Transaction cancelled
    # 4. Transaction failed
    
    today = datetime.datetime.now
    shipped_date = models.DateTimeField(default=today, blank=True)
    received_date = models.DateTimeField(default=today, blank=True)
    cancelled_date = models.DateTimeField(default=today, blank=True)
    failed_date = models.DateTimeField(default=today, blank=True)
    
    TRANSACTION_UNINITIATED = 0
    TRANSACTION_INCOMPLETE = 1
    TRANSACTION_COMPLETE = 2
    TRANSACTION_CANCELLED = 3
    TRANSACTION_FAILED = 4

    TRANSACTION_STATUSES = [(TRANSACTION_UNINITIATED, 'Transaction uninitiated'),(TRANSACTION_INCOMPLETE, 'Transaction incomplete'),(TRANSACTION_COMPLETE, 'Transaction complete'),(TRANSACTION_CANCELLED, 'Transaction cancelled'),(TRANSACTION_CANCELLED, 'Transaction failed')]
    
    status = models.IntegerField(choices=TRANSACTION_STATUSES, default=0)

    def update_status(self, status):
        self.status = status
        if status == 1:
            self.shipped_date = models.DateTimeField(added_now=True)
        if status == 2:
            self.received_date = models.DateTimeField(added_now=True)
        if status == 3:
            self.cancelled_date = models.DateTimeField(added_now=True)
        if status == 4:
            self.failed_date = models.DateTimeField(added_now=True)
    
    def get_status(self):
        return str(self.status)
      
