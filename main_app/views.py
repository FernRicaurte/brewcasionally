from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Brew, Snack
from .forms import EventForm
import requests

def home(request):
    beers = []
    if 'abv' in request.GET:
        abv = request.GET['abv']
    if abv.isdigit():
        api_url = f'https://api.punkapi.com/v2/beers?abv_gt={abv}'
    response = requests.get(api_url)
    if response.status_code == 200:
        beers = response.json()
    return render(request, 'home.html', {'beers': beers})

def about(request):
    return render(request, 'about.html')

def brews_index(request):
    brews = Brew.objects.all()
    return render(request, 'brews/index.html', { 'brews' : brews })

def brews_detail(request, brew_id):
    brew = Brew.objects.get(id=brew_id)
    id_list = brew.snacks.all().values_list('id')
    snack_brew_doesnt_have = Snack.objects.exclude(id__in=id_list)
    event_form = EventForm()
    return render(request, 'brews/detail.html', { 'brew' : brew, 'event_form' : event_form, 'snacks': snack_brew_doesnt_have })

def add_event(request, brew_id):
    form = EventForm(request.POST)
    if form.is_valid():
        new_event = form.save(commit=False)
        new_event.brew_id = brew_id
        new_event.save()
    return redirect('detail', brew_id=brew_id)

def assoc_snack(request, brew_id, snack_id):
    Brew.objects.get(id=brew_id).snacks.add(snack_id)
    return redirect('detail', brew_id=brew_id)

class BrewCreate(CreateView):
    model = Brew
    fields = ['name', 'style', 'abv']

class BrewUpdate(UpdateView):
    model = Brew
    fields = ['name', 'style', 'abv']

class BrewDelete(DeleteView):
    model = Brew
    success_url = '/brews/index'

class SnackCreate(CreateView):
    model = Snack
    fields = ['name', 'description']

class SnackList(ListView):
    model = Snack

class SnackDetail(DetailView):
    model = Snack

class SnackUpdate(UpdateView):
    model = Snack
    fields = ['name', 'description']

class SnackDelete(DeleteView):
    model = Snack
    success_url = '/snacks/'


