from django.shortcuts import render
from .models import News, Category, Comment, Contact
from django.db.models import Q


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
    popular_news = News.objects.all().order_by('-created_at')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')

        if name and email and text:
            Comment.objects.create(
                news=news,
                name=name,
                email=email,
                text=text,
            )

    return render(request, 'single.html', {
        'news': news,
        'categories': categories,
        'popular_news': popular_news,
    })


def category(request, id):
    news = News.objects.filter(category_id=id).order_by('-created_at')
    categories = Category.objects.all()
    current_category = Category.objects.get(id=id)
    popular_news = News.objects.all().order_by('-created_at')

    return render(request, 'category.html', {
        'news': news,
        'categories': categories,
        'current_category': current_category,
        'popular_news': popular_news,
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

def contact(request):
    categories = Category.objects.all()
    popular_news = News.objects.all().order_by('-created_at')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        urgency = request.POST.get('urgency')
        message = request.POST.get('message')

        if first_name and last_name and email and urgency and message:
            Contact.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                urgency=urgency,
                message=message,
            )

    return render(request, 'contact-us.html', {
        'categories': categories,
        'popular_news': popular_news,
    })

def search(request):
    query = request.GET.get('q', '')

    news = News.objects.all().order_by('-created_at')

    if query:
        news = news.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    categories = Category.objects.all()
    popular_news = News.objects.all().order_by('-created_at')

    return render(request, 'search.html', {
        'news': news,
        'categories': categories,
        'popular_news': popular_news,
        'query': query,
    })

def about(request):
    categories = Category.objects.all()
    popular_news = News.objects.all().order_by('-created_at')

    return render(request, 'page.html', {
        'categories': categories,
        'popular_news': popular_news,
    })