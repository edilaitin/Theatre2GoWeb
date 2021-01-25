from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.db.models import Avg
from django.views.generic import ListView, DetailView
from friendship.models import Friend
from star_ratings.models import Rating

from artists.models import UserFollow
from theatres.models import Theatre


class TheatreListView(ListView):
    model = Theatre
    context_object_name = 'theatres'

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Theatre.objects.all()
            theatre_type = self.request.GET.get('type')
            if theatre_type:
                queryset = queryset.filter(theatreType__type__exact=theatre_type).distinct()

            keywords = self.request.GET.get('q')
            if keywords:
                query = SearchQuery(keywords)
                name_vector = SearchVector('name', weight='A')
                artist_vector = SearchVector('artist__name', weight='B')
                vectors = name_vector + artist_vector
                queryset = queryset.annotate(rank=SearchRank(vectors, query)) \
                    .filter(rank__gte=0.3).order_by('-rank').distinct()

            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            count = Friend.objects.unrejected_request_count(user=self.request.user)
            context["f_count"] = count

        theatre_type = self.request.GET.get('type', None)
        if theatre_type is not None:
            context['type'] = theatre_type

        keywords = self.request.GET.get('q')
        if keywords:
            context['query'] = keywords

        return context


class TheatreDetailView(DetailView):
    model = Theatre
    context_object_name = 'theatre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            count = Friend.objects.unrejected_request_count(user=self.request.user)
            context["f_count"] = count

        theatre = self.get_object()
        if self.request.user.is_authenticated:
            try:
                context['follows'] = UserFollow.objects.get(user=self.request.user).theatres.filter(
                    pk=theatre.id).exists()
            except UserFollow.DoesNotExist:
                context['follows'] = False

        vault_play_ids = []

        for vault_play in theatre.vaultplay_set.all():
            vault_play_ids.append(vault_play.id)

        print(vault_play_ids)
        try:
            context['general_rating'] = round(Rating.objects
                                            .filter(object_id__in=vault_play_ids)
                                            .aggregate(Avg('average'))['average__avg'], 1)
        except:
            context['general_rating'] = "No play added yet"

        return context
