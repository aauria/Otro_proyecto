from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Docente
from .form import Docenteform
from django.views.generic import ListView,CreateView,DeleteView,UpdateView


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

class lista_docente(ListView):
    model = Docente
    template_name = 'consulta.html'

class crear_docente(CreateView):
    model = Docente
    form_class = Docenteform
    template_name = 'formulario.html'
    success_url = reverse_lazy('home')

class update_docente(UpdateView):
    model = Docente
    form_class = Docenteform
    template_name = 'formulario.html'
    success_url = reverse_lazy('consulta')

class delete_docente(DeleteView):
    model = Docente
    template_name = 'verificar.html'
    success_url = reverse_lazy('consulta')


def editar_docente(request,id):
    docente=Docente.objects.get(id=id)
    if request.method=='GET':
            form=Docenteform(instance=docente)
            contexto={
                'form':form
            }
    else:
        form=Docenteform(request.POST,instance=docente)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('consulta')
    return render(request, 'formulario.html', contexto)

def eliminar(request,id):
    docente = Docente.objects.get(id=id)
    docente.delete()
    return redirect('consulta')

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
