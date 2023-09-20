from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

def registro(request):
    return render(request,"App1/registro.html")

def inicio(request):
   return render(request, "App1/inicio.html")

def Blogs(request):
    return render(request, "App1/Blogs.html")

def ParaTi(request):
    return render(request, "App1/ParaTi.html")

def Noticias(request):
    return render(request, "App1/Noticias.html")    


def singup(requst):
    pass

def usuario(request):
    pass

def informacion(request):
    pass

# Create your views here.
