from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import registroF

def registro(request):
    if request.method== "POST":

        formRegistro= registroF(request.POST)
        print(formRegistro)

        if formRegistro.is_valid:
            infoR= formRegistro.cleaned_data
            Usuario= usuario(request.POST['nombre'],(request.PSOT['password'], (request.POST[email])))
            Usuario.save()
            return render(request, "App1/registro.html")
            
    else:
        formRegistro = registroF()

    return render(request, "App1/registro.html", {"formRegistro":formRegistro})
    
    



def Home(request):
   return render(request, "App1/Home.html")

def Blogs(request):
    return render(request, "App1/Blogs.html")

def ParaTi(request):
    return render(request, "App1/ParaTi.html")

def Noticias(request):
    return render(request, "App1/Noticias.html")    


def singup(requst):
    if request.method == "POST":
        form= AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form-cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(roquest, user)
                return render(request, 'App1/Home.html', {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, 'App1/singup.html', {"mensaje": f"Error, datos incorrectos"})

        else:
            return render(request, "App1/singup.html", {"mensaje": f"Error, formulario erroneo"})

def usuario(request):
    pass

def informacion(request):
    pass

# Create your views here.
