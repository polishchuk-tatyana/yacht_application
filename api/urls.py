from django.urls import path, include


urlpattens = [
    path('v0/', include('api.v0.urls')),
]
