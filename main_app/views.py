from django.shortcuts import render
from .models import Brew


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def brews_index(request):
    brews = Brew.objects.all()
    return render(request, 'brews/index.html', { 'brews' : brews })
