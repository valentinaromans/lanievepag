from django.urls import path
from . import views

app_name = 'heladeria'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about-us/', views.about_us, name='about_us'),
    path('recomendaciones/', views.recomendaciones, name='recomendaciones'),
]