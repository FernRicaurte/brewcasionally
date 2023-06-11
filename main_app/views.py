from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Brew


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def brews_index(request):
    brews = Brew.objects.all()
    return render(request, 'brews/index.html', { 'brews' : brews })

def brews_detail(request, brew_id):
    brew = Brew.objects.get(id=brew_id)
    return render(request, 'brews/detail.html', { 'brew' : brew })

class BrewCreate(CreateView):
    model = Brew
    fields = '__all__'

class BrewUpdate(UpdateView):
    model = Brew
    fields = '__all__'

class BrewDelete(DeleteView):
    model = Brew
    success_url = '/brews'
