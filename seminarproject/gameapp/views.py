from django.shortcuts import render
from django.http import HttpResponse
from random import choice
from .forms import GameCoinform


def index(request):
    return HttpResponse("Hello, world !")


def coin(request, size: int = 1):
    # return HttpResponse([choice(['решка', 'орёл']) for i in range(size))
    lst = [choice(['решка', 'орёл']) for i in range(size)]
    print(lst)
    return render(request, 'gameapp/coin.html', {'lst': lst})

def dice(request):
    pass


def game_choice(requests):
    if requests.method == 'POST':
        form = GameCoinform(requests.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            size = form.cleaned_data['size']
            if game == 'coin':
                return coin(requests, size)
    else:
        form = GameCoinform()
    return render(requests, 'gameapp/game.html', {'form': form})
