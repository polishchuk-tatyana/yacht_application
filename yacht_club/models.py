# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.signals import post_save


class Club(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)  # This field type is a guess.
    telno = models.CharField(max_length=15)

    '''def __str__(self):
        return "%s %s" % (self.id, self.country)'''

    class Meta:
        managed = False
        db_table = 'club'


class DataYacht(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True)
    type = models.TextField()  # This field type is a guess.
    model = models.CharField(max_length=100)
    max_human = models.IntegerField()
    paid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_yacht'


class Lease(models.Model):
    yacht = models.ForeignKey('Yacht', models.DO_NOTHING, db_column='yacht')
    users = models.ForeignKey('Users', models.DO_NOTHING, db_column='users')
    pay_method = models.TextField()  # This field type is a guess.
    rent_start = models.DateField()
    rent_finish = models.DateField()
    capitan = models.BooleanField()
    certification = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lease'

    '''def save(self, *args, **kwargs):
        finish = self.rent_finish
        start = self.rent_start
        new_paid = self.yacht.paid
        self.new_paid = new_paid
        self.finish = finish
        self.start = start
        self.new_paid = self.new_paid * (self.finish - self.start)



        super(Lease, self).save(*args, **kwargs)'''


class Manufacturer(models.Model):
    name = models.CharField(max_length=300)
    telno = models.CharField(max_length=15)
    country = models.CharField(max_length=20)
    address = models.TextField()  # This field type is a guess.
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacturer'


class Owner(models.Model):
    surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    telno = models.CharField(max_length=15)
    email = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'owner'


class Service(models.Model):
    service = models.CharField(max_length=300)
    telno = models.CharField(max_length=15)
    country = models.CharField(max_length=20)
    address = models.TextField()  # This field type is a guess.
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service'


class Serviceyacht(models.Model):
    service = models.OneToOneField(Service, models.DO_NOTHING, db_column='service', primary_key=True)
    yacht = models.ForeignKey('Yacht', models.DO_NOTHING, db_column='yacht')
    comment = models.CharField(max_length=300, blank=True, null=True)
    start_date = models.DateField()
    finish_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'serviceyacht'
        unique_together = (('service', 'yacht'),)


class Users(models.Model):
    surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    age = models.IntegerField()
    telno = models.CharField(max_length=15)
    email = models.CharField(max_length=50, blank=True, null=True)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=8)

    '''def __str__(self):
        return self.id'''

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('login', 'password'),)


class Worker(models.Model):
    surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    position = models.TextField()  # This field type is a guess.
    salary = models.TextField()  # This field type is a guess.
    telno = models.CharField(max_length=15)
    email = models.CharField(max_length=50, blank=True, null=True)
    club = models.ForeignKey(Club, models.DO_NOTHING, db_column='club')
    manager = models.ForeignKey('self', models.DO_NOTHING, db_column='manager', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worker'


class Yacht(models.Model):
    type = models.TextField()  # This field type is a guess.
    model = models.CharField(max_length=100)
    cabin = models.IntegerField(blank=True, null=True)
    max_human = models.IntegerField()
    year = models.IntegerField()
    length = models.CharField(max_length=10, blank=True, null=True)
    motor = models.CharField(max_length=10, blank=True, null=True)
    club = models.ForeignKey(Club, models.DO_NOTHING, db_column='club')
    manufacturer = models.ForeignKey(Manufacturer, models.DO_NOTHING, db_column='manufacturer')
    paid = models.TextField()  # This field type is a guess.
    owner = models.ForeignKey(Owner, models.DO_NOTHING, db_column='owner')

    class Meta:
        managed = False
        db_table = 'yacht'


class Yachtworkers(models.Model):
    worker = models.OneToOneField(Worker, models.DO_NOTHING, db_column='worker', primary_key=True)
    yacht = models.ForeignKey(Yacht, models.DO_NOTHING, db_column='yacht')

    class Meta:
        managed = False,
        db_table = 'yachtworkers'
        unique_together = (('worker', 'yacht'),)


'''def summa_paid(sender, instance, created, **kwargs):
    paid = instance.paid
    all_paid = Lease.objects.filter(paid=paid)
    sum = 0
    for i in all_paid:
        sum += i.new_paid
    instance.paid.new_paid = sum
    instance.paid.save(force_update=True)


post_save.connect(summa_paid, sender=Lease)
'''