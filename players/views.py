from django.shortcuts import render

from django.http import HttpResponse


def home_page_players(request):
    return HttpResponse("Players page")
