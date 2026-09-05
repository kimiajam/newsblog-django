from django.shortcuts import render
from .models import News


def home(request):
    news = News.objects.all().order_by('-created_at')

    europe = News.objects.filter(category__name='Europe')
    american = News.objects.filter(category__name='Americas')
    africa = News.objects.filter(category__name='Africa')
    asia = News.objects.filter(category__name='Asia')

    return render(request, 'index.html', {
        'news': news,
        'europe': europe,
        'american': american,
        'africa': africa,
        'asia': asia,
    })

def news_detail(request, id):
    news = News.objects.get(id=id)

    return render(request, 'single.html', {
        'news': news,
    })

def category(request, id):
    news = News.objects.filter(category_id=id).order_by('-created_at')

    return render(request, 'category.html', {
        'news': news,
    })
