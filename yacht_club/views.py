from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .forms import *
from .models import *
from django.shortcuts import redirect
from django.http import JsonResponse
# Create your views here.


def registration(request):
    form = RegistrationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()
    return render(request, 'pages/registration.html', locals())


def home(request):

    return render(request, 'pages/home.html', locals())


def reservation_yacht(request):
    form = ReservationYacht(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()
    return render(request, 'pages/reservation_yacht.html', locals())


def reservation(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    yacht_id = data.get('yacht_id')
    yacht_model = data.get('yacht_model')
    yacht_paid = data.get('yacht_paid')
    new_yacht = DataYacht.objects.create(session_key=session_key,id=yacht_id, model=yacht_model, paid=yacht_paid)
    # return_dict['new_yacht'] = new_yacht

    return JsonResponse({'new_yacht': new_yacht})
    # return render(return_dict, 'pages/reservation.html', locals())


def yachts(request):
    yachts = Yacht.objects.filter()
    return render(request, 'pages/yachts.html', locals())


def yacht(request, yacht_id):
    yacht_one = 1
    yacht_two = 2
    yacht_four = 4
    yacht = Yacht.objects.get(id=yacht_id)

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