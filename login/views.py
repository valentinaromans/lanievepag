from django.shortcuts import render

# Create your views here.
def login1(request):
    return render(request, 'login/usuarios.html')
