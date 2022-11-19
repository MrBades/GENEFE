from ast import For
from email import message
from functools import total_ordering
from multiprocessing import context
from multiprocessing.sharedctypes import Value
from statistics import mode
from threading import active_count
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
#from django.utils.encoding import force_text
from django.utils.encoding import force_str
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages

import datetime
from django.urls import reverse_lazy
from django.db.models import Q, F
from django.db.models import Sum
from datetime import date

from .models import Products, Payment, AboutUs
from .forms import AddressForm, ContactForm

from http.client import HTTPResponse
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest

# Create your views here.
def index(request): 
    hom = Home.objects.all()
    product = Products.objects.all()
    context = {
        'homes': hom, 
        'products': Products.objects.all()
    }
    return render(request, 'products/home.html', context)


def products(request): 
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)


def buy_product(request: HttpRequest, ref: str) -> HTTPResponse:    
    product = get_object_or_404(Products, ref = ref)
    address_Form = AddressForm(request.POST)
    if address_Form.is_valid():
        address = address_Form.save()
        p = Payment.objects.create(
            amount = product.price,
            prodRef = product.ref,
            addressTo = address.location,
            email = address.email
        )
        payment = get_object_or_404(Payment, prodRef = ref, id =p.id)
        while not payment.ref:
            payment.ref = secrets.token_urlsafe(50)
            if not Payment.objects.filter(ref=payment.ref):
                tempref = secrets.token_urlsafe(50)
                payment.ref = tempref
            payment.save()
        context={
                 'payment': payment,  
                'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY, 
            }    
        return render(request, 'paystack/make_payment.html', context)
    context = {
        'address': address_Form,
        'product': product
    }
    return render(request, 'paystack/initiate_payment.html', context)


def verify_payment(request: HttpRequest, id: str) -> HTTPResponse:
    # payment = get_object_or_404(Payment, id = id)
    # if payment.verified == False:
    #     payment.verified = True
    #     payment.save()
    #     messages.error(request, 'Succesfully verified transaction')
    
    # else:
    #     messages.error(request, 'Error verifying transaction')

    return render(request, 'paystack/transaction_status.html', {'amount': payment.amount})
        

def about_us(request): 
    about = AboutUs.objects.get(id=1)
    return render(request, 'products/about.html', {'abt': about.about})


def contact_us(request): 
    contact_Form = ContactForm(request.POST)
    if contact_Form.is_valid():
        contact = contact_Form.save()
        messages.error(request, 'Thanks for contacting us')
    return render(request, 'products/contact.html', {'contact': contact_Form})

    