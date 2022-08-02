from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'layout/auth/index.html')

def dashboard(request):
    return HttpResponse('Dashboard')

def register(request):
    return render(request, 'layout/auth/register.html')
    
def home(request):
    return HttpResponse('Home')