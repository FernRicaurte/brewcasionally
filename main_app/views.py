from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Brew, Snack
from .forms import EventForm
import requests

@login_required
def home(request):
    beers = []
    abv = None
    api_url = 'https://api.punkapi.com/v2/beers'  # Default URL
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

@login_required
def brews_index(request):
    brews = Brew.objects.filter(user=request.user)
    return render(request, 'brews/index.html', { 'brews' : brews })

@login_required
def brews_detail(request, brew_id):
    brew = Brew.objects.get(id=brew_id)
    id_list = brew.snacks.all().values_list('id')
    snack_brew_doesnt_have = Snack.objects.exclude(id__in=id_list)
    event_form = EventForm()
    return render(request, 'brews/detail.html', { 'brew' : brew, 'event_form' : event_form, 'snacks': snack_brew_doesnt_have })

@login_required
def add_event(request, brew_id):
    form = EventForm(request.POST)
    if form.is_valid():
        new_event = form.save(commit=False)
        new_event.brew_id = brew_id
        new_event.save()
    return redirect('detail', brew_id=brew_id)

@login_required
def assoc_snack(request, brew_id, snack_id):
    Brew.objects.get(id=brew_id).snacks.add(snack_id)
    return redirect('detail', brew_id=brew_id)

class BrewCreate(LoginRequiredMixin, CreateView):
    model = Brew
    fields = ['name', 'style', 'abv']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class BrewUpdate(LoginRequiredMixin, UpdateView):
    model = Brew
    fields = ['name', 'style', 'abv']

class BrewDelete(LoginRequiredMixin, DeleteView):
    model = Brew
    success_url = '/brews/index'

class SnackCreate(LoginRequiredMixin, CreateView):
    model = Snack
    fields = ['name', 'description']

class SnackList(LoginRequiredMixin, ListView):
    model = Snack

class SnackDetail(LoginRequiredMixin, DetailView):
    model = Snack

class SnackUpdate(LoginRequiredMixin, UpdateView):
    model = Snack
    fields = ['name', 'description']

class SnackDelete(LoginRequiredMixin, DeleteView):
    model = Snack
    success_url = '/snacks/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


