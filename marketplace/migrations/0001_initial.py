# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('bitcoin_cost', models.FloatField()),
                ('quantity_available', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=11)),
                ('publickey', models.TextField()),
                ('bitcoin_credit', models.FloatField()),
                ('accounts', models.TextField()),
                ('rating', models.IntegerField(default=0)),
                ('is_seller', models.BooleanField(default=False)),
                ('purchases', models.ForeignKey(to='marketplace.Listing')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('body', models.TextField()),
                ('opened', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(related_name='message_recipient', to='marketplace.Merchant')),
                ('sender', models.ForeignKey(related_name='message_sender', to='marketplace.Merchant')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('product', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('buyer', models.CharField(max_length=11)),
                ('seller', models.CharField(max_length=11)),
                ('shipped_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('received_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('cancelled_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('failed_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('status', models.IntegerField(choices=[(0, 'Transaction uninitiated'), (1, 'Transaction incomplete'), (2, 'Transaction complete'), (3, 'Transaction cancelled'), (3, 'Transaction failed')], default=0)),
            ],
        ),
    ]
