from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def home(request):
    if request.method == 'GET':
        name_boy = request.GET.get('name_boy')
        name_girl = request.GET.get('name_girl')
        print(f'имя парня: {name_boy}, имя девушки: {name_girl}')
    context = {
        'name_boy': name_boy,
        'name_girl': name_girl,
    }
    return render(request, 'main/index.html', context)
