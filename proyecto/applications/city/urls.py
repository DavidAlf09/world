from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "city_app"

urlpatterns = [
        path('Nuevocity/',
                views.Nuevocity.as_view(),
                name='Nuevocity'),
        path('TrabajoAPISerializer/',
                views.TrabajoAPISerializer.as_view(),
                name='TrabajoAPISerializer'),
        path('cityAPISerializer/',
                views.cityAPISerializer.as_view(),
                name='cityAPISerializer'),
]