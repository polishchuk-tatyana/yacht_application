from django.conf.urls import url, include
from django.contrib import admin
from yacht_club import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('registration_users/', views.registration, name='registration'),
    path('', views.home, name='home'),
    path('yachts/', views.yachts, name='yachts'),
    path('yacht/(?P<yacht_id>\w+)/$', views.yacht, name='yacht'),
    path('login/', views.login_in, name='login_in'),
    path('home_for_user/', views.home_for_user, name='home_for_user'),
    path('reservation/', views.reserv_yacht, name='reserv_yacht'),
    # замена на другой адрес
    path('registration_yacht_yacht/', views.reservation, name='reservation'),
    path('registration_yacht/', views.registration_yacht, name='registration_yacht'),
    # path('registration_yacht_yacht/', views.registration_yacht_yacht, name="registration_yacht_yacht")
    path('bron_owner/', views.bron_owner, name='bron_owner'),
    path('admin_page/', views.admin, name='admin'),
    # изменение пользователя
    path('admin_page/index_user', views.index_user),
    path('admin_page/create_user/', views.create_user),
    path('admin_page/edit_user/<int:id>/', views.edit_user),
    path('admin_page/delete_user/<int:id>/', views.delete_user),
    # изменение работника
    path('admin_page/index_worker', views.index_worker),
    path('admin_page/create_worker/', views.create_worker),
    path('admin_page/edit_worker/<int:id>/', views.edit_worker),
    path('admin_page/delete_worker/<int:id>/', views.delete_worker),
path('yt/', views.yt,),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
