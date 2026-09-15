from django.shortcuts import render
from .models import News, Category


def home(request):
    news = News.objects.all().order_by('-created_at')

    europe = News.objects.filter(category__name='Europe')
    american = News.objects.filter(category__name='Americas')
    africa = News.objects.filter(category__name='Africa')
    asia = News.objects.filter(category__name='Asia')

    categories = Category.objects.all()

    return render(request, 'index.html', {
        'news': news,
        'europe': europe,
        'american': american,
        'africa': africa,
        'asia': asia,
        'categories': categories,
    })

def news_detail(request, id):
    news = News.objects.get(id=id)
    categories = Category.objects.all()

    return render(request, 'single.html', {
        'news': news,
        'categories': categories,
    })


def category(request, id):
    news = News.objects.filter(category_id=id).order_by('-created_at')
    categories = Category.objects.all()
    current_category = Category.objects.get(id=id)

    return render(request, 'category.html', {
        'news': news,
        'categories': categories,
        'current_category': current_category,
    })

def author(request, id):
    from django.contrib.auth.models import User

    user = User.objects.get(id=id)
    news = News.objects.filter(author=user).order_by('-created_at')
    categories = Category.objects.all()

    return render(request, 'author.html', {
        'user': user,
        'profile': user.profile,
        'news': news,
        'categories': categories,
    })