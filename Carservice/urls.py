"""Carservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
import datetime as dt

from Carservice import settings
from cars.models import Car


def index(request):
    car = Car.objects.all().last()
    now = dt.datetime.now()
    car_count = Car.objects.filter(order__datetime__lt=now).distinct().count()
    cars = Car.objects.all()
    if car_count == 0:
        car_count = Car.objects.filter().count()
    context = {'page': 'home', 'cars': cars, 'car': car, 'car_count': car_count}
    return render(request, 'index.html', context=context)


urlpatterns = [
    path('', index, name='main'),
    path('admin/', admin.site.urls),
    path("admin-panel/", include("authentication.urls")),  # Auth routes - login / register
    path("admin-panel/", include("adminpanel.urls")),
    path('cars/', include('cars.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
