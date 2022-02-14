import email
from pyexpat import model
from django import forms
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class registroUser(UserCreationForm):
    email = forms.EmailField()
    telefono = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["username", "email", "telefono", "password1", "password2"]
