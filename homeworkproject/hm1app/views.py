from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(requests):
    logger.info('Index page accessed')
    return HttpResponse('''<h1>Впрервые!!</h1>
    <h2>Попытка стать повелителем Django</h2>
    <p><h2>от несравненного меня</h2></p>
    <p><b>тук-тук-тук</b> - это постучал по дереву</p>''')


def about(requests):
    logger.info('About page accessed')
    return HttpResponse('''<h2> О Себе: </h2>
    <ul>Характер : Нордический</ul>
    <ul>Возраст : Не совсем стар</ul>
    <ul>Ленивость : Повышенная</ul>''')

# Create your views here.
