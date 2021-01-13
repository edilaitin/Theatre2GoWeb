from django.shortcuts import render
from django.views.generic import ListView, DetailView

from theatres.models import Theatre


class TheatreListView(ListView):
    model = Theatre
    context_object_name = 'theatres'


class TheatreDetailView(DetailView):
    model = Theatre
    context_object_name = 'theatre'
