from django.urls import path
from . import views

urlpatterns = [
    path('heads/', views.head_tails, name='head_tails'),
    path('cube/', views.cube, name='cube'),
    path('number/', views.rand_number, name='rand_number'),
]