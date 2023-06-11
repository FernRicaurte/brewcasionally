from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('brews/index', views.brews_index, name='index'),
path('brews/<int:brew_id>/', views.brews_detail, name='detail'),
path('brews/create/', views.BrewCreate.as_view(), name='brews_create'),
]