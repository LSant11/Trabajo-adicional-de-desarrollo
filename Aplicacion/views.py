from django.shortcuts import render,HttpResponse,redirect
from .models import Ferreteria, Usuario
from .forms import ferreform 


# Create your views here.




def Home (request):
    return render(request,"aplicacion/Home.html")

def servicios  (request):
    return  render(request,"aplicacion/Servicio.html")

def tienda (request):
    return  render(request,"Aplicacion/Tienda.html")

def registrate (request):
    return  render(request,"aplicacion/Registrate.html")

def Bas (request):
    return  render(request,"aplicacion/Bas.html")

def funcion (request):
    return render (request,"aplicacion/funcion.html")

def ferreteria (request):
    ferreteria= Ferreteria.objects.all()
    return render (request,"ferreteria/index.html", {'ferreteria': ferreteria})

def crear (request):
    formulario = ferreform(request.POST or None , request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect ('ferreteria')
    return render (request,"ferreteria/crear.html", {'formulario': formulario})

def editar (request,id):
    ferreteria=Ferreteria.objects.get(id=id)
    formulario=ferreform(request.POST or None , request.FILES or None ,instance=ferreteria)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect ('ferreteria')
    return render (request,"ferreteria/editar.html", {'formulario': formulario})

def eliminar (request,id):
    ferreteria= Ferreteria.objects.get(id=id)
    ferreteria.delete()
    return redirect ('ferreteria')

def index (request):
    return render (request,"ferreteria/index.php")

def header (request):
    return render (request,"ferreteria/header.php")