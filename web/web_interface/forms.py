from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=15, label_suffix='')
    password1 = forms.CharField(label='Password', label_suffix='', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password',label_suffix='', widget=forms.PasswordInput())
    
    def clean(self):
        if self.cleaned_data.get('password1') != None and len(self.cleaned_data.get('password1')) < 8:
            self.add_error('password1','Password must be 8 or more characters')
        if self.cleaned_data.get('password1') != self.cleaned_data.get('password2'):
            self.add_error('password2','Passwords much match')
        return self.cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=15, label_suffix='')
    password = forms.CharField(label='Password', label_suffix='', widget=forms.PasswordInput())
