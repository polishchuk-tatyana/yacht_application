from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .forms import *
from .models import *
from django.shortcuts import redirect
from django.core import serializers
from django.http import JsonResponse
# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.messages import error as ms_error
from django.views.generic.list import ListView
import datetime
from django.db import connection
from .forms import *
from .models import *
from datetime import datetime, date


def registration(request):
    form = RegistrationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()
    return render(request, 'pages/registration.html', locals())


def home(request):

    return render(request, 'pages/home.html', locals())


def reservation(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    yacht_id = data.get('yacht_id')
    yacht_model = data.get('yacht_model')
    yacht_paid = data.get('yacht_paid')
    yacht_max_human = data.get('yacht_max_human')
    yacht_type = data.get('yacht_type')
    new_yacht = DataYacht.objects.create(session_key=session_key,id=yacht_id, model=yacht_model, paid=yacht_paid, max_human=yacht_max_human,type=yacht_type)

    yachts = DataYacht.objects.filter(session_key=session_key)
    yachts_nb = yachts.count()
    return_dict['yachts_nb'] = yachts_nb
    return_dict['yachts'] = list()

    for item in yachts:
        yacht_dict = dict()
        yacht_dict['model'] = item.model
        yacht_dict['paid'] = item.paid
        yacht_dict['max_human'] = item.max_human
        yacht_dict['type'] = item.type
        return_dict['yachts'].append(yacht_dict)

    return JsonResponse(return_dict)


def reserv_yacht(request):
    session_key = request.session.session_key
    bron_yachts = DataYacht.objects.filter(session_key=session_key)

    form = ReservationYacht(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()

    return render(request, 'pages/reservation.html', locals())


def yachts(request):
    yachts = Yacht.objects.filter()
    return render(request, 'pages/yachts.html', locals())


def yacht(request, yacht_id):
    yacht_one = 1
    yacht_two = 2
    yacht_four = 4
    yacht = Yacht.objects.get(id=yacht_id)
    days = Lease.objects.filter()
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'pages/yacht.html', locals())


def login(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()
    return render(request, 'pages/login.html', locals())


def registration_yacht(request):
    form = RegistrationYacht()
    yacht_formset = YachtFormset(instance=Owner())

    if request.POST:
        form = RegistrationYacht(request.POST)
        if form.is_valid():
            owner = form.save()
            yacht_formset = YachtFormset(request.POST, instance=owner)

            if yacht_formset.is_valid():
                yacht_formset.save()

            return redirect('/registration_yacht/')

    return render(request, 'pages/registration_yacht.html', locals())