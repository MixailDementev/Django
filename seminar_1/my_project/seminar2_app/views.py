from django.http import HttpResponse
from django.shortcuts import render
from random import randint

from seminar2_app.models import GameModel


def index(request):
    result = ('TAILS', 'HEADS')[randint(0, 1)]
    game = GameModel(result=result)
    game.save()

    return HttpResponse(f'{game}')

def last_games(request):
    last = GameModel().return_last(5)
    last_str = ['<br>' + str(i) for i in last]
    return HttpResponse(last_str)