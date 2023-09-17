from django.http import HttpResponse
from django.shortcuts import render

from seminar2_book_app.models import Author


def author(request):
    res = Author.objects.all()
    res_str = ['<br>' + str(i) for i in res]
    return HttpResponse(res_str)


