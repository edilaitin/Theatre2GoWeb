from django.urls import path
from artists.views import ArtistListView, ArtistDetailView
from plays.views import PlayListView, PlayDetailView

urlpatterns = [
    path('', PlayListView.as_view(), name='plays_view'),
    path('<int:pk>/', PlayDetailView.as_view(), name="play_view")
]