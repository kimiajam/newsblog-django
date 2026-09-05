from django.contrib import admin
from .models import News, Profile, Category

admin.site.register(News)
admin.site.register(Profile)
admin.site.register(Category)