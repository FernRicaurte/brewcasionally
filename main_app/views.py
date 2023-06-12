from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Brew, Snack
from .forms import EventForm
import requests

def home(request):
    return render(request, 'home.html')

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
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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

def signup(request):
    error_message = ''
    if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
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


