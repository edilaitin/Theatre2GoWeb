from django.contrib import admin

from artists.models import Artist, ActorRole
from plays.admin import ActorsInline


# class ActorRoleAdmin(admin.ModelAdmin)


class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Artist, ArtistAdmin)
admin.site.register(ActorRole)
