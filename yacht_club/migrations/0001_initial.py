# Generated by Django 3.1 on 2020-09-22 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('address', models.TextField(blank=True, null=True)),
                ('telno', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'club',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_method', models.TextField()),
                ('rent_start', models.DateField()),
                ('rent_finish', models.DateField()),
                ('capitan', models.BooleanField()),
                ('paid', models.TextField()),
                ('certification', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lease',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('telno', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'manufacturer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=300)),
                ('telno', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SumProfit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('прибыль_всех_яхты', models.TextField(blank=True, db_column='Прибыль всех яхты', null=True)),
            ],
            options={
                'db_table': 'sum_profit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('telno', models.CharField(max_length=15)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('position', models.TextField()),
                ('salary', models.TextField()),
                ('telno', models.CharField(max_length=15)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'worker',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Yacht',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
                ('image', models.ImageField(upload_to='static/media/yacht_images')),
                ('model', models.CharField(max_length=100)),
                ('cabin', models.IntegerField(blank=True, null=True)),
                ('max_human', models.IntegerField()),
                ('year', models.IntegerField()),
                ('length', models.CharField(blank=True, max_length=10, null=True)),
                ('motor', models.CharField(blank=True, max_length=10, null=True)),
                ('paid', models.TextField()),
            ],
            options={
                'db_table': 'yacht',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Serviceyacht',
            fields=[
                ('service', models.OneToOneField(db_column='service', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='yacht_club.service')),
                ('comment', models.CharField(blank=True, max_length=300, null=True)),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
            ],
            options={
                'db_table': 'serviceyacht',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Yachtworkers',
            fields=[
                ('worker', models.OneToOneField(db_column='worker', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='yacht_club.worker')),
                ('yacht', models.ForeignKey(db_column='yacht', on_delete=django.db.models.deletion.DO_NOTHING, to='yacht_club.yacht')),
            ],
            options={
                'db_table': 'yachtworkers',
                'managed': (False,),
                'unique_together': {('worker', 'yacht')},
            },
        ),
    ]