from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('brews/index', views.brews_index, name='index'),
path('brews/<int:brew_id>/', views.brews_detail, name='detail'),
path('brews/create/', views.BrewCreate.as_view(), name='brews_create'),
path('brews/<int:pk>/update/', views.BrewUpdate.as_view(), name='brews_update'),
path('brews/<int:pk>/delete/', views.BrewDelete.as_view(), name='brews_delete'),
path('brews/<int:brew_id>/add_event/', views.add_event, name='add_event'),
]