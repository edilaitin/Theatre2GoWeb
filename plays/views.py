from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.views.generic import ListView, DetailView

from artists.models import UserFollow
from plays.models import Play


class PlayListView(ListView):
    model = Play
    context_object_name = 'plays'

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Play.objects.all()

            keywords = self.request.GET.get('q')
            if keywords:
                query = SearchQuery(keywords)
                title_vector = SearchVector('vaultPlay__title', weight='A')
                theatre_vector = SearchVector('vaultPlay__theatre__name', weight='B')
                vectors = title_vector + theatre_vector
                queryset = queryset.annotate(rank=SearchRank(vectors, query)) \
                    .filter(rank__gte=0.2).order_by('-rank').distinct()

            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        keywords = self.request.GET.get('q')
        if keywords:
            context['query'] = keywords

        return context


class PlayDetailView(DetailView):
    model = Play
    context_object_name = 'play'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            try:
                context['follows'] = UserFollow.objects.get(user=self.request.user).plays.filter(pk=self.get_object().vaultPlay.id).exists()
            except UserFollow.DoesNotExist:
                context['follows'] = False

        return context
