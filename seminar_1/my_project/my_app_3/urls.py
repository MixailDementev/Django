from django.urls import path
from . import views


urlpatterns = [
    # path('', views.MainPageView.as_view(), name='main_page'),
    # path('about/', views.AboutView.as_view(), name='about_page'),
    path('site/', views.site, name='main_page'),
    path('author/', views.author, name='about_page'),
]