from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'heladeria/inicio.html')


def about_us(request):
    return render(request, 'heladeria/about_us.html')

def recomendaciones(request):
    return render(request, 'heladeria/recomendaciones.html')
