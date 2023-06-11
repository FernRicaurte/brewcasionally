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
    path('snacks/', views.SnackList.as_view(), name='snacks_list'),
    path('snacks/<int:pk>/', views.SnackDetail.as_view(), name='snacks_detail'),
    path('snacks/create/', views.SnackCreate.as_view(), name='snacks_create'),
    path('snacks/<int:pk>/update/', views.SnackUpdate.as_view(), name='snacks_update'),
    path('snacks/<int:pk>/delete/', views.SnackDelete.as_view(), name='snacks_delete'),
    path('brews/<int:brew_id>/assoc_snack/<int:snack_id>/', views.assoc_snack, name='assoc_snack')
]