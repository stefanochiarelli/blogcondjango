
from statistics import mode
from django import forms
# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CommentModel, Post

class ContactoForm(forms.Form):
    usuario = forms.CharField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ["usuario_post"]
        fields = [ 'usuario_email', 'usuario_mensaje']
        labels = {
            'usuario_email': 'Tu Email',
            'usuario_mensaje': 'Mensaje'

        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =  '__all__'



class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modifica tu E-mail")
    password1 = forms.CharField(label="Constraseña")
    password2 = forms.CharField(label="Repita su Constraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name','last_name']