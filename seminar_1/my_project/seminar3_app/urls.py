
from django.urls import path

from .views import HomeViews, AboutViews, HeadsGame, DiceGame, AllPostViews, DetailPost

urlpatterns = [
    path('home/', HomeViews.as_view(), name='home_page'),
    path('about/', AboutViews.as_view(), name='about_page'),
    path('game1/<int:count>', HeadsGame.as_view(), name='game1_page'),
    path('game2/<int:count>', DiceGame.as_view(), name='game2_page'),
    path('posts/<int:id_author>', AllPostViews.as_view(), name='posts'),
    path('posts_author/<int:pk>', DetailPost.as_view(), name='posts_author'),
]