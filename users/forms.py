from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    '''
This class is to add an email field and make sure whenever a user is created, it is of type models.User and the order of fields is as per given in Meta class.
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']