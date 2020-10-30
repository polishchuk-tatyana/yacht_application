from django.shortcuts import render
from .forms import RegistrationForm, LoginForm
from .models import *
# Create your views here.


def registration(request):
    form = RegistrationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()
    return render(request, 'pages/registration.html', locals())


def home(request):

    return render(request, 'pages/home.html', locals())


def favorites(request):

    return render(request, 'pages/favorites.html', locals())


def registration_yacht(request):

    return render(request, 'pages/registration_yacht.html', locals())


def reservation(request):

    return render(request, 'pages/reservation.html', locals())


def yachts(request):
    yachts = Yacht.objects.filter()
    return render(request, 'pages/yachts.html', locals())


def yacht(request, yacht_id):
    yacht_one = 1
    yacht_two = 2
    yacht_four = 4
    yacht = Yacht.objects.get(id=yacht_id)
    return render(request, 'pages/yacht.html', locals())


def login(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()
    return render(request, 'pages/login.html', locals())