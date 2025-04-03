from django.contrib import admin
from django.urls import path,include
from . import views
from agri import views
app_name = 'agri'
urlpatterns = [
     path('',views.predict_crop,name='agri'),
     path('predict/', views.predict_crop, name='predict_crop'),
     path('fertilizer-predict/', views.fert_recommend, name='fertilizer_predict'),
     path('request-soil-test/', views.request_soil_test, name='request_soil_test'),
     path('track-soil-test/', views.track_soil_test, name='track_soil_test'),
     path('generate-pdf/<uuid:tracking_id>/', views.generate_pdf, name='generate_pdf'),
]
app_name = 'agri'

 #path('cropresult/',views.cropinfo,name='cropresult'),
     #path('maincon/',views.maincon,name='maincon'),


