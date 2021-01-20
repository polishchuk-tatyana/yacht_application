from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
import datetime
from django.db import connection
from .forms import *
from .models import *
from datetime import datetime, date
from django.contrib.auth.models import Group, User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

'''Изменение пользователя'''

# получение данных из бд
def index_user(request):
    people = Users.objects.all()
    return render(request, "pages/index_user.html", {"people": people})

# изменение данных в бд
def edit_user(request, id):
    try:
        person = Users.objects.get(id=id)

        if request.method == "POST":
            person.surname = request.POST.get("surname")
            person.firstname = request.POST.get("firstname")
            person.age = request.POST.get("age")
            person.telno = request.POST.get("telno")
            person.save()
            return render(request, 'pages/index_user.html', locals())
        else:
            return render(request, "pages/edit_user.html", {"person": person})
    except Users.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete_user(request, id):
    try:
        person = Users.objects.get(id=id)
        person.delete()
        return render(request, 'pages/index_user.html', locals())
    except Users.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

'''Изменение работника'''

# получение данных из бд
def index_worker(request):
    people = Worker.objects.all()
    return render(request, "pages/index_worker.html", {"people": people})

# изменение данных в бд
def edit_worker(request, id):
    try:
        person = Worker.objects.get(id=id)

        if request.method == "POST":
            person.surname = request.POST.get("surname")
            person.firstname = request.POST.get("firstname")
            person.position = request.POST.get("position")
            person.salary = request.POST.get("salary")
            person.telno = request.POST.get("telno")
            person.email = request.POST.get("email")
            person.club = request.POST.get("club")
            person.manager = request.POST.get("manager")
            person.save()
            return render(request, 'pages/index_worker.html', locals())
        else:
            return render(request, "pages/edit_worker.html", {"person": person})
    except Worker.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete_worker(request, id):
    try:
        person = Worker.objects.get(id=id)
        person.delete()
        return render(request, 'pages/index_worker.html', locals())
    except Worker.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")




'''Изменение владельца'''

# получение данных из бд
def index_owner(request):
    people = Owner.objects.all()
    return render(request, "pages/index_owner.html", {"people": people})

# изменение данных в бд
def edit_owner(request, id):
    try:
        person = Owner.objects.get(id=id)

        if request.method == "POST":
            person.surname = request.POST.get("surname")
            person.firstname = request.POST.get("firstname")
            person.telno = request.POST.get("telno")
            person.save()
            return render(request, 'pages/index_owner.html', locals())
        else:
            return render(request, "pages/edit_owner.html", {"person": person})
    except Owner.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete_owner(request, id):
    try:
        person = Owner.objects.get(id=id)
        person.delete()
        return render(request, 'pages/index_owner.html', locals())
    except Owner.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


'''Изменение клуба'''

# получение данных из бд
def index_club(request):
    people = Club.objects.all()
    return render(request, "pages/index_club.html", {"people": people})

# изменение данных в бд
def edit_club(request, id):
    try:
        person = Club.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.country = request.POST.get("country")
            person.address = request.POST.get("address")
            person.telno = request.POST.get("telno")
            person.save()
            return render(request, 'pages/index_club.html', locals())
        else:
            return render(request, "pages/edit_club.html", {"person": person})
    except Club.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete_club(request, id):
    try:
        person = Club.objects.get(id=id)
        person.delete()
        return render(request, 'pages/index_club.html', locals())
    except Club.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


'''Изменение яхты'''

# получение данных из бд
def index_yacht(request):
    people = Yacht.objects.all()
    return render(request, "pages/index_yacht.html", {"people": people})

# изменение данных в бд
def edit_yacht(request, id):
    try:
        person = Yacht.objects.get(id=id)

        if request.method == "POST":
            person.type = request.POST.get("type")
            person.model = request.POST.get("model")
            person.cabin = request.POST.get("cabin")
            person.max_human = request.POST.get("max_human")
            person.year = request.POST.get("year")
            person.length = request.POST.get("length")
            person.motor = request.POST.get("motor")
            person.club = request.POST.get("club")
            person.manufacturer = request.POST.get("manufacturer")
            person.paid = request.POST.get("paid")
            person.owner = request.POST.get("owner")
            person.save()
            return render(request, 'pages/index_yacht.html', locals())
        else:
            return render(request, "pages/edit_yacht.html", {"person": person})
    except Yacht.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete_yacht(request, id):
    try:
        person = Yacht.objects.get(id=id)
        person.delete()
        return render(request, 'pages/index_yacht.html', locals())
    except Yacht.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")



'''Изменение бронирований'''

# получение данных из бд
def index_lease(request):
    people = Lease.objects.all()
    return render(request, "pages/index_lease.html", {"people": people})

# изменение данных в бд
def edit_lease(request, id):
    try:
        person = Lease.objects.get(id=id)

        if request.method == "POST":
            person.yacht = request.POST.get("yacht")
            person.users = request.POST.get("users")
            person.pay_method = request.POST.get("pay_method")
            person.rent_start = request.POST.get("rent_start")
            person.rent_finish = request.POST.get("rent_finish")
            person.capitan = request.POST.get("capitan")
            person.certification = request.POST.get("certification")

            person.save()
            return render(request, 'pages/index_lease.html', locals())
        else:
            return render(request, "pages/edit_lease.html", {"person": person})
    except Lease.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete_lease(request, id):
    try:
        person = Lease.objects.get(id=id)
        person.delete()
        return render(request, 'pages/index_lease.html', locals())
    except Lease.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


'''Изменение производителя'''

# получение данных из бд
def index_manufacturer(request):
    people = Manufacturer.objects.all()
    return render(request, "pages/index_manufacturer.html", {"people": people})

# изменение данных в бд
def edit_manufacturer(request, id):
    try:
        person = Manufacturer.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.country = request.POST.get("country")
            person.address = request.POST.get("address")
            person.telno = request.POST.get("telno")
            person.email = request.POST.get("email")
            person.save()
            return render(request, 'pages/index_manufacturer.html', locals())
        else:
            return render(request, "pages/edit_manufacturer.html", {"person": person})
    except Manufacturer.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete_manufacturer(request, id):
    try:
        person = Manufacturer.objects.get(id=id)
        person.delete()
        return render(request, 'pages/index_manufacturer.html', locals())
    except Manufacturer.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


"""----------------------------------------------------------------"""

def admin(request):
    if request.user.groups.filter(name = 'Administrator').exists():
        return render(request, 'pages/admin_page.html', locals())

    return render(request, 'pages/admin_page.html', locals())


def registration(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'pages/home_for_user.html', locals())
    else:
        user_form = UserRegistrationForm()
    return render(request, 'pages/registration.html', locals())


def login_in(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            return render(request, 'pages/home_for_user.html', locals())
        else:
            messages.add_message(request, messages.INFO, 'Неверные логин или пароль')
        if not request.user.is_authenticated:
            context = {'message': "Такого пользователя нет"}
    return render(request, 'pages/login.html', locals())


def login_out(request):
    logout(request)
    return redirect('pages/home.html')


def home_for_user(request):
    return render(request, 'pages/home_for_user.html', locals())


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
        if request.user.is_authenticated():
            # user = Users.objects.get(Login=request.user.username)
            date = datetime.now()
            data = form.cleaned_data
            new_form = form.save()

    return render(request, 'pages/reservation.html', locals())


def bron_owner(request):
    session_key = request.session.session_key
    bron_yachts = DataYacht.objects.filter(session_key=session_key)

    return render(request, 'pages/bron_owner.html', locals())


def yacht(request, yacht_id):
    dateq=date(datetime.now().year, datetime.now().month, datetime.now().day)

    yacht_one = 1
    yacht_two = 2
    yacht_four = 4
    yacht = Yacht.objects.get(id=yacht_id)
    days = Lease.objects.filter()
    user = Users.objects.filter()
    session_key = request.session.session_key

    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'pages/yacht.html', locals())


def yachts(request):
    yachts = Yacht.objects.filter()
    return render(request, 'pages/yachts.html', locals())



def yt(request):
    form_worker = FormWorker(request.POST or None)
    club = Club.objects.filter()
    if request.method == 'POST' and form_worker.is_valid():
        data = form_worker.cleaned_data
        new_form = form_worker.save()
    return render(request, 'pages/yt.html', locals())

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

    if request.method == 'POST':
        owner_form = UserRegistrationForm(request.POST)
        if owner_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = owner_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(owner_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'pages/home_for_user.html', locals())
    else:
        owner_form = UserRegistrationForm()
    return render(request, 'pages/registration_yacht.html', locals())

def addUser(request):
    form_user = RegistrationForm(request.POST or None)
    if request.method == 'POST' and form_user.is_valid():
        data = form_user.cleaned_data
        new_form = form_user.save()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            new_user.groups.add(Group.objects.get(name='User'))
            return render(request, 'pages/admin_page.html', locals())
    else:
        user_form = UserRegistrationForm()
    return render(request, 'pages/add_user.html', locals())


def addWorker(request):
    form_user = FormWorker(request.POST or None)
    if request.method == 'POST' and form_user.is_valid():
        data = form_user.cleaned_data
        new_form = form_user.save()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            new_user.groups.add(Group.objects.get(name='Worker'))
            return render(request, 'pages/admin_page.html', locals())
    else:
        user_form = UserRegistrationForm()
    return render(request, 'pages/add_worker.html', locals())


def addOwner(request):
    form_user = RegistrationYacht(request.POST or None)
    if request.method == 'POST' and form_user.is_valid():
        data = form_user.cleaned_data
        new_form = form_user.save()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            new_user.groups.add(Group.objects.get(name='Owner'))
            return render(request, 'pages/admin_page.html', locals())
    else:
        user_form = UserRegistrationForm()
    return render(request, 'pages/add_owner.html', locals())


def addManager(request):
    form_user = FormWorker(request.POST or None)
    if request.method == 'POST' and form_user.is_valid():
        data = form_user.cleaned_data
        new_form = form_user.save()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            new_user.groups.add(Group.objects.get(name='Manager'))
            return render(request, 'pages/admin_page.html', locals())
    else:
        user_form = UserRegistrationForm()
    return render(request, 'pages/add_owner.html', locals())