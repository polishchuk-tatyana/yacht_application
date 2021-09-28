from django.urls import path, include

urlpattens = [
    path('user/', include('api.v0.user.urls')),
    path('organization/', include('api.v0.organization.urls')),
]
