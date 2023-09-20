from django.urls import path
from AplicacionRegistro import views
from AplicacionRegistro.views import *


urlpatterns = [ 
    path('inicio/', views.inicio, name="inicio"),
    path('',views.registro,name="registro"),
    path('singup/',views.singup,name="singup"),
    path('Noticias/',views.Noticias,name="Noticias"),
    path('Blogs/',views.Blogs,name="Blogs"),
    path('ParaTi/',views.ParaTi,name="ParaTi"),


]   