# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path

from adminpanel.views import *

urlpatterns = [

    # The home page
    path('', car, name='home'),
    path('profile', profile, name='profile'),
    path('car', car, name='admin-car'),
    path('driver', driver, name='admin-driver'),
    path('add-car', add_car, name='admin-add-car'),
    path('add-driver', add_driver, name='admin-add-driver'),
    path('car/update/<int:id>', update_car),
    path('driver/update/<int:id>', update_driver),
    path('car/delete/<int:id>', delete_car),
    path('driver/delete/<int:id>', delete_driver),
    path('contacts', contactforms, name='contactforms'),
    path('requests', requests, name='requests'),
    path('contact/delete/<int:contact_id>', delete_contact_form, ),

    # Matches any html file

]
