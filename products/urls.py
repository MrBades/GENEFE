from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.products, name='products'),
    path('about/', views.about_us, name='about'),
    path('contact/', views.contact_us, name='contact'),
    path('api/session/<ref>/', views.buy_product, name='buy'),
    
    
    path('api/session/<str:id>/', views.verify_payment, name='verify'),
]
