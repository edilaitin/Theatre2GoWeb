from django.contrib.postgres.aggregates import StringAgg
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.views.generic import ListView, DetailView
from friendship.models import Friend

from artists.models import Artist, UserFollow


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

            keywords = self.request.GET.get('q')
            if keywords:
                query = SearchQuery(keywords)
                name_vector = SearchVector('name', weight='A')
                theatre_vector = SearchVector(StringAgg('associatedTheatres__name', delimiter=' '), weight='B')
                play_vector = SearchVector(StringAgg('actorrole__vaultPlay__title', delimiter=' '), weight='B')
                vectors = name_vector + theatre_vector + play_vector
                queryset = queryset.annotate(rank=SearchRank(vectors, query)) \
                    .filter(rank__gte=0.2).order_by('-rank').distinct()

            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artist_type = self.request.GET.get('type', None)
        if artist_type is not None:
            context['type'] = artist_type

        if self.request.user.is_authenticated:
            count = Friend.objects.unrejected_request_count(user=self.request.user)
            context["f_count"] = count

        keywords = self.request.GET.get('q')
        if keywords:
            context['query'] = keywords

        return context


class ArtistDetailView(DetailView):
    model = Artist
    context_object_name = 'artist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            count = Friend.objects.unrejected_request_count(user=self.request.user)
            context["f_count"] = count

        if self.request.user.is_authenticated:
            try:
                context['follows'] = UserFollow.objects.get(user=self.request.user).artists.filter(pk=self.get_object().id).exists()
            except UserFollow.DoesNotExist:
                context['follows'] = False

        return context

