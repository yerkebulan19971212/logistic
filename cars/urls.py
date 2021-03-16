from django.urls import path
from .views import *


urlpatterns = [
    path('order/', create_order, name="create_order"),
    path('contacts/', contact, name='contact'),
    path('service/', service, name='service'),
    path('about/', about, name='about'),
    path('cars/', cars, name='cars'),
    path('blog/', blog, name='blog'),

]
