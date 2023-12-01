from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "countrylanguage_app"

urlpatterns = [
        path('Nuevocountrylanguage/',
                views.Nuevocountrylanguage.as_view(),
                name='Nuevocountrylanguage'),
        path('TrabajoAPISerializer/',
                views.TrabajoAPISerializer.as_view(),
                name='TrabajoAPISerializer'),
        path('countrylanguageAPISerializer/',
                views.countrylanguageAPISerializer.as_view(),
                name='countrylanguageAPISerializer'),
]