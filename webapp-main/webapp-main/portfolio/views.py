from django.shortcuts import render, redirect

def index(request):

    return render(request, 'index.html')

def home(request):
    
    return render(request, 'home.html')

def about(request):
    
    return render(request, 'about.html')

def services(request):
    
    return render(request, 'services.html')

def portfolio(request):
    
    return render(request, 'portfolio.html')
def contact(request):
    
    return render(request, 'contact.html')