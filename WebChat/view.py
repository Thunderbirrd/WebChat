from django.shortcuts import render


def home(request):
    title = 'Главная'
    return render(request, 'index.html')
