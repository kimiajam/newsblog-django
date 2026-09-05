from django.shortcuts import render
from .models import News


def home(request):
    news = News.objects.all().order_by('-created_at')

    europe = News.objects.filter(category__name='Europe')
    american = News.objects.filter(category__name='American')
    africa = News.objects.filter(category__name='Africa')
    asia = News.objects.filter(category__name='Asia')

    return render(request, 'index.html', {
        'news': news,
        'europe': europe,
        'american': american,
        'africa': africa,
        'asia': asia,
    })