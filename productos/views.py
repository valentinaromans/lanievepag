from django.shortcuts import render

# Create your views here.
def catalogo(request):
    return render(request, 'productos/catalogo.html')