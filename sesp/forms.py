from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.http import request


class UserForm(ModelForm):
    #last_name = forms.CharField(blank=False)
    #first_name = forms.CharField(blank=False)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].required = True
        self.fields['first_name'].required = True

    fields = ['basic_field']

class CreateUserForm(UserCreationForm):
    #last_name = forms.CharField(blank=False)
    #first_name = forms.CharField(blank=False)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].required = True
        self.fields['first_name'].required = True
