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
                ('authenticator', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('datecreated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('bitcoin_cost', models.FloatField()),
                ('quantity_available', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=512, default='legacy migrations')),
                ('publickey', models.TextField(blank=True)),
                ('bitcoin_credit', models.FloatField(default=0)),
                ('accounts', models.TextField(blank=True)),
                ('rating', models.IntegerField(default=0)),
                ('is_seller', models.BooleanField(default=False)),
                ('purchases', models.ForeignKey(blank=True, to='marketplace.Listing', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('body', models.TextField()),
                ('opened', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(related_name='message_recipient', to='marketplace.Merchant')),
                ('sender', models.ForeignKey(related_name='message_sender', to='marketplace.Merchant')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('product', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('buyer', models.CharField(max_length=11)),
                ('seller', models.CharField(max_length=11)),
                ('shipped_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('received_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('cancelled_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('failed_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.IntegerField(choices=[(0, 'Transaction uninitiated'), (1, 'Transaction incomplete'), (2, 'Transaction complete'), (3, 'Transaction cancelled'), (3, 'Transaction failed')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='authenticator',
            name='userid',
            field=models.ForeignKey(to='marketplace.Merchant'),
        ),
    ]
