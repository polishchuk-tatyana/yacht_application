from django.contrib import admin
from .models import *
# Register your models here.


class Users_Elements(admin.ModelAdmin):
    list_display = [field.name for field in Users._meta.fields]
    # fields = ["name"]
    list_filter = ['age', ]
    search_fields = ['surname', 'firstname', 'age', 'telno', 'email']

    class Meta:
        model = Users


admin.site.register(Users, Users_Elements)


class Yacht_Elements(admin.ModelAdmin):
    list_display = [field.name for field in Yacht._meta.fields]
    # fields = ["name"]
    search_fields = ['type', 'model', 'cabin', 'max_human', 'year', 'length', 'motor', 'users__surname', 'club__name', 'manufacturer__name', 'paid']

    class Meta:
        model = Yacht


admin.site.register(Yacht, Yacht_Elements)


class Club_Elements(admin.ModelAdmin):
    list_display = [field.name for field in Club._meta.fields]
    # fields = ["name"]
    list_filter = ('name', )

    class Meta:
        model = Club


admin.site.register(Club, Club_Elements)


class Lease_Elements(admin.ModelAdmin):
    list_display = [field.name for field in Lease._meta.fields]
    # fields = ["name"]
    search_fields = ['yacht_model', 'users_surname', 'pay_method', 'rent_start', 'rent_finish', 'capitan', 'paid', 'certification']

    class Meta:
        model = Lease


admin.site.register(Lease, Lease_Elements)

class Manufacturer_Elements(admin.ModelAdmin):
    list_display = [field.name for field in Manufacturer._meta.fields]
    # fields = ["name"]
    search_fields = ['name', 'telno', 'country', 'address', 'email']

    class Meta:
        model = Manufacturer


admin.site.register(Manufacturer, Manufacturer_Elements)


class Service_Elements(admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]
    # fields = ["name"]
    search_fields = ['service', 'telno', 'country', 'address', 'email']

    class Meta:
        model = Service


admin.site.register(Service, Service_Elements)

class ServiceYacht_Elements(admin.ModelAdmin):
    list_display = [field.name for field in Serviceyacht._meta.fields]
    # fields = ["name"]
    search_fields = ['service', 'yacht__model', 'comment', 'start_date', 'finish_date']

    class Meta:
        model = Serviceyacht


admin.site.register(Serviceyacht, ServiceYacht_Elements)


class Worker_Elements(admin.ModelAdmin):
    list_display = [field.name for field in Worker._meta.fields]
    # fields = ["name"]
    search_fields = ['surname', 'firstname', 'position', 'salary', 'telno', 'email', 'club__name', 'manager__surname']

    class Meta:
        model = Worker


admin.site.register(Worker, Worker_Elements)


class Yachtworkers_Elements(admin.ModelAdmin):
    list_display = [field.name for field in Yachtworkers._meta.fields]
    # fields = ["name"]
    search_fields = ['worker__surname', 'yacht__model']

    class Meta:
        model = Yachtworkers


admin.site.register(Yachtworkers, Yachtworkers_Elements)
