from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from .forms import RegistroForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required# from django.http import HttpResponse

# Create your views here.

def primero(request):
    return render(request,"iniciar_secion.html")

def bienvenida(request):
    return render(request,"bienvenida.html")

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.direccion = form.cleaned_data['direccion']
            usuario.sexo = form.cleaned_data['sexo']
            usuario.save()
            form.save_m2m()
            login(request, usuario)
            return redirect('/')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

