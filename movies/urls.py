from django.urls import path
from movies.views import MovieCreateListView, MovieRetrieveDestroyAPIView

app_name='Movies'

urlpatterns = [
    path('movies/', MovieCreateListView.as_view(), name='MovieCreateListView'),
    path('movies/<int:pk>', MovieRetrieveDestroyAPIView.as_view(), name='MovieRetrieveDestroyAPIView'),
]