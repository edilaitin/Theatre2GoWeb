from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_theatres, name='view_theatres'),
]