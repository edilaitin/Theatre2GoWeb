from django.urls import path
from artists.views import ArtistListView, ArtistDetailView

urlpatterns = [
    path('', ArtistListView.as_view(), name='artists_view'),
    path('<int:pk>/', ArtistDetailView.as_view(), name="artist_view")
]