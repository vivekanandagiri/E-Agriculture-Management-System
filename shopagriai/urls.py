from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
#from Agriexpert.Agriexpert import settings
from django.conf import settings
from . import views
from shopagriai import views
urlpatterns = [
    
    
    path('',views.shop,name='shop'),
    
    path('viewcategory/',views.category,name='viewcategory'),   
    path('category/<str:category_name>/', views.category_view, name='category_view'),
    path('product/<int:id>/', views.product_detail_view, name='product_detail'),
    path('cart/',views.cart,name='cart'),
    path('update_item/', views.updateItem, name="update_item"),
    path('checkout/',views.checkout,name='checkout'),
    path('process_order/',views.processOrder,name='process_order'),
    path('process-order/', views.processOrder, name='process_order'),
    path('order-success/<str:transaction_id>/', views.order_success, name='order_success'), 
    path('my-orders/', views.user_orders, name='user_orders'),   
    path('search/', views.search_products, name='search_products'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
     #path('', views.home, name='home'),
     #path('viewproduct/',views.viewproduct,name='viewproduct'),








