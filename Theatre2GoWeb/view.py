import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render

from artists.models import UserFollow, Artist
from plays.models import VaultPlay, Play
from theatres.models import Theatre

from friendship.models import Friend


def home(request):
    if request.user.is_authenticated:
        count = Friend.objects.unrejected_request_count(user=request.user)

        try:
            user_follow = UserFollow.objects.get(user=request.user)
        except UserFollow.DoesNotExist:
            UserFollow.objects.create(user=request.user)
            user_follow = UserFollow.objects.get(user=request.user)
        plays = Play.objects.filter(startTime__gt=datetime.date.today() - datetime.timedelta(days=1)).order_by(
            "startTime")

        relevant_plays = []
        for play in plays:
            if play in user_follow.plays.all():
                relevant_plays.append(play)
            elif play.vaultPlay.theatre in user_follow.theatres.all():
                relevant_plays.append(play)
            else:
                for actor in play.vaultPlay.actorrole_set.all():
                    if actor.artist in user_follow.artists.all():
                        relevant_plays.append(play)
                        break

        if not relevant_plays:
            relevant_plays = plays
        context = {
            "plays": relevant_plays,
            "f_count": count,
            "from_home": True
        }
        return render(request, 'plays/play_list.html', context)
    else:
        context = {
            "plays": Play.objects.filter(startTime__gt=datetime.date.today() - datetime.timedelta(days=1)).order_by(
                "startTime"),
            "from_home": True
        }
        return render(request, 'plays/play_list.html', context)


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

