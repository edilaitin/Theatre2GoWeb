from django.shortcuts import render
from django.http import HttpResponse

from theatres.models import Theatre


def view_theatres(request):
    context = {
        'theatres': Theatre.objects.all()
    }
    return render(request, "theatres/index.html", context)
