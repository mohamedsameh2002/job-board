from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User   (athor way)
from .models import Profile,User




class SinupForm (UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class UserForm (forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['phone_numper','imag',]

