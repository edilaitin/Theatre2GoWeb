from django.views.generic import ListView, DetailView

from artists.models import Artist


class ArtistListView(ListView):
    model = Artist
    context_object_name = 'artists'

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Artist.objects.all()
            artist_type = self.request.GET.get('type', None)
            if artist_type is not None:
                if artist_type == "actor":
                    queryset = queryset.filter(actorrole__isnull=False).distinct()
                elif artist_type == "director":
                    queryset = queryset.filter(director__isnull=False).distinct()
            return queryset


class ArtistDetailView(DetailView):
    model = Artist
    context_object_name = 'artist'
