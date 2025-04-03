from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
#from Agriexpert.Agriexpert import settings
from django.conf import settings
from . import views
from myapp import views
from .views import  otp_verify,change_password, view_profile,edit_profile
urlpatterns = [
    
    path('',views.authregister,name='authregister'),
    path('index/',views.IndexPage,name='index'),
    path('otp/home/',views.HomePage,name='home'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('base/',views.basePage,name='base'),
    path('authlogin/',views.authlogin,name='authlogin'),
    path('main/',views.mainpage,name='mainpage'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('otp/', views.otpVerify, name='otp'),
    path('otp-verify/', views.otp_verify, name='otp_verify'),
    path('soil-track/',views.soil_track,name='soil_track'),
    path('change_password/', change_password, name='change_password'),
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('weather/', views.weather_view, name='weather_view'),
    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
     #path('', views.home, name='home'),
#path('otp-login/',views.otp_login, name='otp_login'),




