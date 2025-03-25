from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Júlio Cesar', 'age': '36',
    })

def contato(request):
    return render(request, 'global/home.html')

def sobre(request):
    return HttpResponse('SOBRE')
