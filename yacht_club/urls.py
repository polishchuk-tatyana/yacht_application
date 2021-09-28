from django.conf.urls import url
from django.contrib import admin
from yacht_club import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('registration_users/', views.registration, name='registration'),
                  path('', views.home, name='home'),
                  path('yachts/', views.yachts, name='yachts'),
                  path('yacht/(?P<yacht_id>\w+)/$', views.yacht, name='yacht'),
                  path('login/', views.login_in),
                  path('home_for_user/', views.home_for_user, name='home_for_user'),
                  path('reservation/', views.reserv_yacht, name='reserv_yacht'),
                  # замена на другой адрес
                  path('registration_yacht_yacht/', views.reservation, name='reservation'),
                  path('registration_yacht/', views.registration_yacht, name='registration_yacht'),
                  path('registration_owner/', views.registration_owner, name="registration_owner"),
                  path('bron_owner/', views.bron_owner, name='bron_owner'),
                  path('admin_page/', views.admin, name='admin'),
                  # изменение пользователя
                  path('admin_page/index_user', views.index_user),
                  path('admin_page/edit_user/<int:id>/', views.edit_user),
                  path('admin_page/delete_user/<int:id>/', views.delete_user),
                  # изменение работника
                  path('admin_page/index_worker', views.index_worker),
                  path('admin_page/edit_worker/<int:id>/', views.edit_worker),
                  path('admin_page/delete_worker/<int:id>/', views.delete_worker),
                  # изменение owner
                  path('admin_page/index_owner', views.index_owner),
                  path('admin_page/edit_owner/<int:id>/', views.edit_owner),
                  path('admin_page/delete_owner/<int:id>/', views.delete_owner),
                  # изменение club
                  path('admin_page/index_club', views.index_club),
                  path('admin_page/edit_club/<int:id>/', views.edit_club),
                  path('admin_page/delete_club/<int:id>/', views.delete_club),
                  # изменение yacht
                  path('admin_page/index_yacht', views.index_yacht),
                  path('admin_page/edit_yacht/<int:id>/', views.edit_yacht),
                  path('admin_page/delete_yacht/<int:id>/', views.delete_yacht),
                  # изменение lease
                  path('admin_page/index_lease', views.index_lease),
                  path('admin_page/edit_lease/<int:id>/', views.edit_lease),
                  path('admin_page/delete_lease/<int:id>/', views.delete_lease),
                  # изменение manufacturer
                  path('admin_page/index_manufacturer', views.index_manufacturer),
                  path('admin_page/edit_manufacturer/<int:id>/', views.edit_manufacturer),
                  path('admin_page/delete_manufacturer/<int:id>/', views.delete_manufacturer),

                  path('admin_page/add_user/', views.addUser),
                  path('admin_page/add_worker/', views.addWorker),
                  path('admin_page/add_owner/', views.addOwner),
                  path('admin_page/add_manager/', views.addManager),
                  path('admin_page/add_club/', views.addClub),
                  path('admin_page/add_yacht/', views.addYacht),
                  path('admin_page/add_yachtworkers/', views.addYachtworker),
                  path('admin_page/add_lease/', views.addLease),
                  path('admin_page/add_manufacturer/', views.addManufacturer),

                  # изменение работника
                  path('manager/index_worker', views.index_worker),
                  path('manager/edit_worker/<int:id>/', views.edit_worker),
                  path('manager/delete_worker/<int:id>/', views.delete_worker),

                  # изменение lease
                  path('manager/index_lease', views.index_lease),
                  path('manager/edit_lease/<int:id>/', views.edit_lease),
                  path('manager/delete_lease/<int:id>/', views.delete_lease),

                  # изменение owner
                  path('manager/index_owner', views.index_owner),
                  path('manager/edit_owner/<int:id>/', views.edit_owner),
                  path('manager/delete_owner/<int:id>/', views.delete_owner),

                  # изменение пользователя
                  path('manager/index_user', views.index_user),
                  path('manager/edit_user/<int:id>/', views.edit_user),
                  path('manager/delete_user/<int:id>/', views.delete_user),

                  path('manager/add_worker/', views.addWorker),
                  path('manager/add_user/', views.addUser),
                  path('manager/add_owner/', views.addOwner),
                  path('manager/add_lease/', views.addLease),

                  path('manager/', views.manager),
                  path('api/', include('api.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
