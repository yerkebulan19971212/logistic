from django import forms

from cars.models import *
from .models import *


# class FormCreate(forms.ModelForm):
#     class Meta:
#         model = ContactForm
#         fields = ['name', 'email', 'phone', 'description']


class CarsCreate(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['photo', 'driver', 'mark', 'color', 'number']


class DriverCreate(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'gender']

# class IssueCreate(forms.ModelForm):
#     class Meta:
#         model = Issue
#         fields = ['insurance', 'fio', 'iin', 'bday', 'doc1', 'doc2', 'doc3', 'phone', 'email']