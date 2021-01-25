from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from friendship.models import Friend, FriendshipRequest


def my_profile(request):
    all_users = User.objects.all()
    sent_requests = Friend.objects.sent_requests(user=request.user)
    received_requests = Friend.objects.unrejected_requests(user=request.user)

    users = [user for user in all_users if
             not Friend.objects.are_friends(request.user, user)
             and user.id != request.user.id
             ]

    filtered_users = []
    keywords = request.GET.get('q')
    if keywords:
        for user in users:
            if user.first_name.__contains__(keywords) or user.last_name.__contains__(keywords):
                filtered_users.append(user)
            elif f"{user.first_name} {user.last_name}".__contains__(keywords):
                filtered_users.append(user)
            elif user.email == keywords:
                filtered_users.append(user)
    else:
        filtered_users = users

    for user in filtered_users:
        if any(r.to_user == user for r in sent_requests):
            user.sent_request = True
        else:
            user.sent_request = False

    for user in filtered_users:
        if any(r.from_user == user for r in received_requests):
            user.received_request = True
        else:
            user.received_request = False

    context = {
        "friends": Friend.objects.friends(request.user),
        "users": filtered_users
    }

    if keywords:
        context["query"] = keywords

    if request.user.is_authenticated:
        count = Friend.objects.unrejected_request_count(user=request.user)
        context["f_count"] = count

    return render(request, "users/myprofile.html", context)


def add_friend(request):
    user_id = request.POST.get("user_id", "")
    Friend.objects.add_friend(
        request.user,
        User.objects.get(pk=user_id)
    )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def friend_requests(request):
    context = {
        "friend_requests": Friend.objects.unrejected_requests(user=request.user)
    }
    return render(request, "users/friend_requests.html", context)


def accept_friend(request):
    req_id = request.POST.get("id", "")
    FriendshipRequest.objects.get(pk=req_id).accept()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def reject_friend(request):
    req_id = request.POST.get("id", "")
    FriendshipRequest.objects.get(pk=req_id).reject()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
