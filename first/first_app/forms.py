from django import forms
from .models import Profile_model
from django.contrib.auth.models import User

class Profile_form(forms.ModelForm):
    class Meta():
        model=Profile_model
        fields=('portfolio_site','profile_pic')
class Userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    password_again=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password','password_again')
class Log_in(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
