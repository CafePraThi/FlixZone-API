from django.urls import path
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView

app_name='Actors'

urlpatterns = [
    path('actors/', ActorCreateListView.as_view(), name='ActorCreateListView'),
    path('actors/<int:pk>', ActorRetrieveUpdateDestroyView.as_view(), name='ActorRetrieveUpdateDestroyView'),
]