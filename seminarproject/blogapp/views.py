from django.shortcuts import render
from django.http import HttpResponse
from .models import Autor
from .forms import AutorForms

# class Autor(models.Model):
#     name = models.CharField(max_length=100)
#     secondname = models.CharField(max_length=100)
#     email = models.EmailField()
#     bio = models.TextField()
#     bday = models.DateField()


def index(requests):
    return HttpResponse('Hello')


def view_autors(requests):
    # for i in range(101):
    #     autor = Autor(name=f'aaaa{i}', secondname=f'bbbb{i}', email=f'aaaaa@{i}.ru', bio=f'ccccccc{i}', bday=f'2023-11-24')
    #     autor.save()
    return HttpResponse('autor')


def post_autor(requests):
    if requests.method == 'POST':
        form = AutorForms(requests.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            secondname = form.cleaned_data['secondname']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            bday = form.cleaned_data['bday']
            autor = Autor(name=name, secondname=secondname, email=email, bio=bio,
                          bday=bday)
            autor.save()
            return render(requests, 'blogapp/postautor.html', {'answer': 'Автор добавлен'})
    else:
        form = AutorForms()

    return render(requests, 'blogapp/postautor.html', {'form': form})