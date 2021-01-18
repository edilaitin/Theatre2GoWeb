from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.views.generic import ListView, DetailView

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
