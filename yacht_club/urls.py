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
    path('login/', views.login, name='login'),
    path('reservation/', views.reserv_yacht, name='reserv_yacht'),
    # замена на другой адрес
    path('registration_yacht_yacht/', views.reservation, name='reservation'),
    path('registration_yacht/', views.registration_yacht, name='registration_yacht'),
    # path('registration_yacht_yacht/', views.registration_yacht_yacht, name="registration_yacht_yacht")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
