from django.contrib import admin
from theatres.models import TheatreType, Theatre, WorkProgram

admin.site.register(TheatreType)
admin.site.register(WorkProgram)
admin.site.register(Theatre)
