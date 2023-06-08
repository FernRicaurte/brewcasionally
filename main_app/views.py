from django.shortcuts import render

brews = [
    {'name': 'Beer 1', 'type': 'Brown Ale', 'abv': 5.0 },
    {'name': 'Beer 2', 'type': 'IPA', 'abv': 6.0 },
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def brews_index(request):
    return render(request, 'brews/index.html', { 'brews' : brews })
