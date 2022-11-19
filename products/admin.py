from django.contrib import admin
from .models import *
# Register your models here.

class productsAdm(admin.ModelAdmin):
     list_display=('name', 'price', 'stock')



class offerAdm(admin.ModelAdmin):
     list_display=('name', 'email', 'message')
     

class AboutUsAdm(admin.ModelAdmin):
     list_display=('about','id')
     

class HomeAdm(admin.ModelAdmin):
     list_display=('title','describtion','img')
     

class PayAdm(admin.ModelAdmin):
     list_display=('amount','addressTo','verified', 'id')
     
     
admin.site.register(Products, productsAdm)     
admin.site.register(Contact, offerAdm)  
admin.site.register(AboutUs, AboutUsAdm)
admin.site.register(Home, HomeAdm)
admin.site.register(Payment, PayAdm)