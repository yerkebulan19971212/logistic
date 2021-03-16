from django.contrib import admin
from .models import *

admin.site.register([Car, Driver, Order, ContactForm])

# Register your models here.
