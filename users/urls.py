from django.urls import path

from users import views

urlpatterns = [
    path('myprofile/', views.my_profile, name='my_profile'),
    path('addfriend/', views.add_friend, name='add_friend'),
    path('friendrequests/', views.friend_requests, name='friend_requests'),
    path('friendrequests/accept', views.accept_friend, name='accept_friend'),
    path('friendrequests/reject', views.reject_friend, name='reject_friend'),
]
