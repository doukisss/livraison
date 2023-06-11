from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def clients_page(request):
    return render(request, 'home.html')

def courriers_page(request):
    return render(request, 'home.html')