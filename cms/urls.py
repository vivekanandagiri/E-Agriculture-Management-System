from django.contrib import admin
from django.urls import path,include
from . import views
from cms import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news,name='news'),
    path('viewnews/<str:slug>',views.viewnews,name='viewnews')
         
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)