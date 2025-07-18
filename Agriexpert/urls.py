"""
URL configuration for Agriexpert project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
admin.site.site_header="AgriAi Admin"
admin.site.site_title="AgriAi Portal"
admin.site.index_title="Welcome to AgriAi "
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
#from Agriexpert.Agriexpert import settings
from django.conf import settings
from . import views
from myapp import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('agri/',include('agri.urls')),
    path('cms/',include('cms.urls')),
    path('',include('myapp.urls')),
    path('shop/',include('shopagriai.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    

    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

