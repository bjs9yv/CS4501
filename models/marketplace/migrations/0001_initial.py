# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authenticator',
            fields=[
                ('authenticator', models.CharField(serialize=False, max_length=128, primary_key=True)),
                ('date_created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('bitcoin_cost', models.FloatField()),
                ('quantity_available', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=11)),
                ('password', models.CharField(default='legacy migrations', max_length=512)),
                ('publickey', models.TextField(blank=True)),
                ('bitcoin_credit', models.FloatField(default=0)),
                ('accounts', models.TextField(blank=True)),
                ('rating', models.IntegerField(default=0)),
                ('is_seller', models.BooleanField(default=False)),
                ('purchases', models.ForeignKey(to='marketplace.Listing', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('opened', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(related_name='message_recipient', to='marketplace.Merchant')),
                ('sender', models.ForeignKey(related_name='message_sender', to='marketplace.Merchant')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('product', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('buyer', models.CharField(max_length=11)),
                ('seller', models.CharField(max_length=11)),
                ('shipped_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('received_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('cancelled_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('failed_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('status', models.IntegerField(default=0, choices=[(0, 'Transaction uninitiated'), (1, 'Transaction incomplete'), (2, 'Transaction complete'), (3, 'Transaction cancelled'), (3, 'Transaction failed')])),
            ],
        ),
        migrations.AddField(
            model_name='authenticator',
            name='user_id',
            field=models.ForeignKey(to='marketplace.Merchant'),
        ),
    ]
