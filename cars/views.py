from django.shortcuts import render, redirect
from .models import Order, Car, Driver, ContactForm
import datetime as dt
from django.db.models import Max
import random
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import random
from django.utils.html import format_html



def contact(request):
    return render(request, 'contact.html', {"page": "contact"})


def service(request):
    return render(request, 'service.html', {"page": "service"})


def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {"page": "cars", "cars": cars})


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
    city_type = request.POST.get('city_type')
    prices = request.POST.get('prices', 0)
    date = request.POST.get('date')
    car = request.POST.get('car')
    time_date_time = request.POST.get('date_to')
    email = request.POST.get('email')
    type_service = request.POST.get('type')
    date_time = dt.datetime.strptime(date, "%Y-%m-%dT%H:%M")

    price_text = 'Цена за услугу :' + str(prices) + 'тг'

    order = Order.objects.create(city_type=city_type, car_id=car, type=type_service, order_time=date,
                                 time=time_date_time, fromm=from_p, to=to, email=email, price=prices)
    messages.info(request, price_text)
            # # messages.error(request, "Барлық данныйларды email-ңізге жбердік")
            # text = "\n".join([order_detals.car.mark, order_detals.fromm, order_detals.to, str(order_detals.time),
            #                   str(order_detals.datetime), order_detals.get_type_display(), ])

    # send_mail(
    #     'Машина жалдау',
    #     text,
    #     settings.EMAIL_HOST_USER,
    #     [email],
    # )

    return redirect('main')


def send_support(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        description = request.POST.get("description")
        ContactForm.objects.create(name=name, phone=phone,
                                   email=email, description=description)
        return redirect('contact')
