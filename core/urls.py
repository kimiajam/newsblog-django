from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django_ckeditor_5 import urls as ck_editor_5_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckeditor5/", include(ck_editor_5_urls)),
    path('', include('news.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)