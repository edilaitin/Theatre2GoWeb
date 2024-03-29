"""Theatre2GoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from Theatre2GoWeb import view

urlpatterns = [
    path('', view.home, name='index'),
    # path('', view.friend_req_count, name='base'),
    path('artists/', include('artists.urls')),
    path('plays/', include('plays.urls')),
    path('theatres/', include('theatres.urls')),
    path('users/', include('users.urls')),

    path('accounts/', include('allauth.urls')),

    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('friendship/', include('friendship.urls')),

    path('follow/', view.follow, name='follow'),
    path('unfollow/', view.unfollow, name='unfollow'),

    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
