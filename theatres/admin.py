from django.contrib import admin
from theatres.models import TheatreType, Theatre, WorkProgram


class WorkProgramInLine(admin.StackedInline):
    model = WorkProgram


class TheatreAdmin(admin.ModelAdmin):
    list_display = ['name', 'theatreType', 'website', 'phone']
    search_fields = ['name']
    list_filter = ['theatreType']
    inlines = [WorkProgramInLine]


admin.site.register(TheatreType)
admin.site.register(Theatre, TheatreAdmin)
