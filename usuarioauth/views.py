from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View
from django.contrib.auth import login, logout
# from django.contrib.auth.forms import UserCreationForm
from .forms import registroUser


# Create your views here.
class registro(View):
    def post(self, response):
        form = registroUser(response.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog-inicio'))
        return render(response, 'usuarioauth/registro.html', {'form': form})

    def get(self, response):   
        form = registroUser()
        return render(response, 'usuarioauth/registro.html', {'form': form})
    