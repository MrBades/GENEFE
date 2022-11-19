from xmlrpc.client import boolean
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import TextInput, Select
from .models import Address, Contact


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address        
        fields = ('phone', 'email', 'location')
        
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
