from django.contrib import admin
from .models import News, Profile, Category, Comment, Contact

admin.site.register(News)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Contact)