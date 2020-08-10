from django.shortcuts import render,redirect
from .models import Docente
from .form import Docenteform

# relaciona la parte vista con el template home.html
def home(request, plantilla="home.html"):
    return render(request, plantilla);
def index(request, plantilla="index.html"):
    return render(request, plantilla);
def about(request, plantilla="about.html"):
    return render(request, plantilla);
def contact(request, plantilla="contact.html"):
    return render(request, plantilla);
def portfolio(request, plantilla="portfolio.html"):
    return render(request, plantilla);
def login(request, plantilla="login.html"):
    return render(request, plantilla);
def correo(request, plantilla="correo.html"):
    return render(request, plantilla);
def formulario(request):
     if request.method=='GET':
         form=Docenteform()
         contexto={
            'form':form
         }
     else:
         form = Docenteform(request.POST)
         contexto = {
             'form': form
         }
         if form.is_valid():
             form.save()
             return redirect ('home')

     return render(request,'formulario.html',contexto)

# Create your views here.
