from django.urls import path
from seminar2_app import views

app_name = 'seminar2_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('last/', views.last_games, name='last_games'),
]