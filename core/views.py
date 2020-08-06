from django.shortcuts import render
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
# Create your views here.
