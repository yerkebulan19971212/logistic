from django.shortcuts import render, redirect
from .models import Order, Car, Driver
import datetime as dt
from django.db.models import Max
import random


def contact(request):
    return render(request, 'contact.html', {"page": "contact"})


def service(request):
    return render(request, 'service.html', {"page": "service"})


def cars(request):
    return render(request, 'cars.html', {"page": "cars"})


def about(request):
    return render(request, 'about.html', {"page": "about"})


def blog(request):
    return render(request, 'blog.html', {"page": "blog"})


def get_random_car(cars):
    max_id = cars.aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        car = Car.objects.filter(pk=pk).first()
        if car:
            return car
    return None


def create_order(request):
    from_p = request.POST.get('from')
    to = request.POST.get('to')
    date = request.POST.get('date')
    email = request.POST.get('email')
    type_service = request.POST.get('type')
    date_time = dt.datetime.strptime(date, "%Y-%m-%d").date()
    cars = Car.objects.filter(order__datetime__date__lte=date_time)
    if cars:
        car = get_random_car(cars)

    if not car:
        pass  # send to email that car is null
    else:
        Order.objects.create(car=car, type=type_service, order_time=date, fromm=from_p, to=to, email=email)

    return redirect('main')
