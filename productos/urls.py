from django.urls import path
from . import views

app_name = 'productos'
urlpatterns = [
    path('catalogo/', views.catalogo, name='catalogo'),
]