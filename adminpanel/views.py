from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from adminpanel.forms import CarsCreate
from cars.models import *


@login_required(login_url="/admin-panel/login/")
def index(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('admin-panel/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/admin-panel/login/")
def profile(request):
    context = {}
    context['segment'] = 'profile'

    html_template = loader.get_template('admin-panel/page-user.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/admin-panel/login/")
def car(request):
    list = Car.objects.all()
    context = {"list": list}
    context['segment'] = 'news'

    html_template = loader.get_template('admin-panel/car.html')
    return HttpResponse(html_template.render(context, request))


def add_car(request):
    upload = CarsCreate()
    if request.method == 'POST':
        upload = CarsCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('/admin-panel/car')
        else:
            return HttpResponse(
                """your form is wrong, reload on <a href = "{{ url : '/admin-panel/news'}}">reload</a>""")
    else:
        list = Driver.objects.all()
        context = {
            "upload_form": upload,
            "list": list,
            "action": "Добавить"
        }
        return render(request, 'admin-panel/add-car.html', context)


@login_required(login_url="/admin-panel/login/")
def update_car(request, id: int):
    try:
        sel = Car.objects.get(pk=id)
    except id.DoesNotExist:
        return redirect('/admin-panel/car')
    form = CarsCreate(request.POST, request.FILES or None, instance=sel)
    if form.is_valid():
        form.save()
        return redirect('/admin-panel/car')
    context = {
        "ProductForm": form,
        "ProductModel": sel,
        "action": "Обновить"
    }
    return render(request, 'admin-panel/add-car.html', context)


@login_required(login_url="/admin-panel/login/")
def delete_car(request, id):
    news_id = int(id)
    try:
        news_sel = Car.objects.get(pk=id)
    except news_id.DoesNotExist:
        return redirect('/admin-panel/car')
    news_sel.delete()
    return redirect('/admin-panel/car')


@login_required(login_url="/admin-panel/login/")
def contactforms(request):
    list = ContactForm.objects.all()
    context = {"list": list}
    context['segment'] = 'contactforms'

    html_template = loader.get_template('admin-panel/contact-forms.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/admin-panel/login/")
def requests(request):
    list = Order.objects.all()
    context = {"list": list}
    context['segment'] = 'requests'

    html_template = loader.get_template('admin-panel/requests.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/admin-panel/login/")
def delete_contact_form(request, contact_id):
    contact_id = int(contact_id)
    try:
        contact_sel = ContactForm.objects.get(pk=contact_id)
    except contact_id.DoesNotExist:
        return redirect('/admin-panel/contacts')
    contact_sel.delete()
    return redirect('/admin-panel/contacts')


@login_required(login_url="/admin-panel/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
