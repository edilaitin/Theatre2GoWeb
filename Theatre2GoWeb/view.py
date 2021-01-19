from django.http import HttpResponseRedirect

from artists.models import UserFollow, Artist
from plays.models import VaultPlay
from theatres.models import Theatre


def follow(request):
    try:
        user_follow = UserFollow.objects.get(user=request.user)
    except UserFollow.DoesNotExist:
        UserFollow.objects.create(user=request.user)
        user_follow = UserFollow.objects.get(user=request.user)

    play_id = request.POST.get("play", "")
    if play_id:
        user_follow.plays.add(VaultPlay.objects.get(pk=play_id))

    theatre_id = request.POST.get("theatre", "")
    if theatre_id:
        user_follow.theatres.add(Theatre.objects.get(pk=theatre_id))

    artist_id = request.POST.get("artist", "")
    if artist_id:
        user_follow.artists.add(Artist.objects.get(pk=artist_id))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unfollow(request):
    try:
        user_follow = UserFollow.objects.get(user=request.user)
    except UserFollow.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    play_id = request.POST.get("play", "")
    if play_id:
        user_follow.plays.remove(VaultPlay.objects.get(pk=play_id))

    theatre_id = request.POST.get("theatre", "")
    if theatre_id:
        user_follow.theatres.remove(Theatre.objects.get(pk=theatre_id))

    artist_id = request.POST.get("artist", "")
    if artist_id:
        user_follow.artists.remove(Artist.objects.get(pk=artist_id))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
