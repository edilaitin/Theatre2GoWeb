from django.views.generic import ListView, DetailView

from theatres.models import Theatre


class TheatreListView(ListView):
    model = Theatre
    context_object_name = 'theatres'

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Theatre.objects.all()
            theatre_type = self.request.GET.get('type', None)
            if theatre_type is not None:
                queryset = queryset.filter(theatreType__type__exact=theatre_type).distinct()
            return queryset


class TheatreDetailView(DetailView):
    model = Theatre
    context_object_name = 'theatre'
