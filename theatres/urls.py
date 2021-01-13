from django.urls import path
from .views import TheatreListView, TheatreDetailView

urlpatterns = [
    path('', TheatreListView.as_view(), name='theatres_view'),
    path('<int:pk>/', TheatreDetailView.as_view(), name="theatre_view")
]