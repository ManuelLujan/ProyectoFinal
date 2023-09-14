from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

def inicio(request):
    return render(request,"App1/index.html")


def registro(request):
    pass


# Create your views here.
