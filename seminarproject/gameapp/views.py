from django.shortcuts import render
from django.http import HttpResponse
from random import choice


def index(request):
    return HttpResponse("Hello, world !")


def coin(request):
    return HttpResponse(choice(['решка', 'орёл']))