from django.shortcuts import render
from django.http import HttpResponse
from .models import Autor

# class Autor(models.Model):
#     name = models.CharField(max_length=100)
#     secondname = models.CharField(max_length=100)
#     email = models.EmailField()
#     bio = models.TextField()
#     bday = models.DateField()


def index(requests):
    return HttpResponse('Hello')


def view_autors(requests):
    for i in range(101):
        autor = Autor(name=f'aaaa{i}', secondname=f'bbbb{i}', email=f'aaaaa@{i}.ru', bio=f'ccccccc{i}', bday=f'2023-11-24')
        autor.save()
    return HttpResponse('autor')