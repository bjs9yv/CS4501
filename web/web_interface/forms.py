from django import forms
from django.core.urlresolvers import reverse

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=15, label_suffix='')
    password1 = forms.CharField(label='Password', label_suffix='', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password',label_suffix='', widget=forms.PasswordInput())
    
    def clean(self):
        if self.cleaned_data.get('password1') != None and len(self.cleaned_data.get('password1')) < 7:
            self.add_error('password1','Password must be 7 or more characters')
        if self.cleaned_data.get('password1') != self.cleaned_data.get('password2'):
            self.add_error('password2','Passwords much match')
        return self.cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=15, label_suffix='')
    password = forms.CharField(label='Password', label_suffix='', widget=forms.PasswordInput())

class CreateListingForm(forms.Form):
    title = forms.CharField(label = 'Listing Title', max_length=30, label_suffix = '' )
    description = forms.CharField(label = 'Description', max_length= 255)
    bitcoin_cost = forms.FloatField(label = 'Item Cost in BitCoin')
    quantity_available = forms.FloatField(label = 'Quantity Available') 
