from django.contrib import admin

from artists.models import ActorRole
from plays.models import VaultPlay, Play


class ActorsInline(admin.StackedInline):
    model = ActorRole


class VaultPlayAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_theatre_name', 'get_director_name']
    search_fields = ['title', 'get_theatre_name', 'get_director_name']
    list_filter = ['active']

    def get_theatre_name(self, obj):
        return obj.theatre.name

    def get_director_name(self, obj):
        return obj.director.name

    get_theatre_name.short_description = "Theatre"
    get_director_name.short_description = "Director"
    inlines = [ActorsInline]


class PlayAdmin(admin.ModelAdmin):
    list_display = ['get_play_name', 'get_theatre_name', 'startTime']
    search_fields = ['get_play_name', 'get_theatre_name']
    ordering = ['-startTime']

    def get_play_name(self, obj):
        return obj.vaultPlay.title

    def get_theatre_name(self, obj):
        return obj.vaultPlay.theatre.name

    get_play_name.short_description = 'Play title'
    get_theatre_name.short_description = "Theatre"


admin.site.register(Play, PlayAdmin)
admin.site.register(VaultPlay, VaultPlayAdmin)
