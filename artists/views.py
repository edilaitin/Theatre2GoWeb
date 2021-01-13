from django.shortcuts import render
from django.views.generic import ListView, DetailView

from artists.models import Artist


class ArtistListView(ListView):
    model = Artist
    context_object_name = 'artists'


class ArtistDetailView(DetailView):
    model = Artist
    context_object_name = 'artist'
