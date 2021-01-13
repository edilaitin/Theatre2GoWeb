from django.views.generic import ListView, DetailView

from plays.models import Play


class PlayListView(ListView):
    model = Play
    context_object_name = 'plays'


class PlayDetailView(DetailView):
    model = Play
    context_object_name = 'play'
