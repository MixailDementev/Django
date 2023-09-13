from django.urls import path
from seminar2_book_app import views

app_name = 'seminar2_book_app'

urlpatterns = [
    path('', views.author, name='author'),
]