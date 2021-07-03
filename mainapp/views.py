from django.shortcuts import render

def index(request):
    context = {
        'page_title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context)

def about_me(request):
    context = {
        'page_title': 'Обо мне',
    }
    return render(request, 'mainapp/about_me.html', context)

def date(request):
     context = {
         'page_title': 'date',
     }
     return render(request, 'mainapp/date.html', context)
