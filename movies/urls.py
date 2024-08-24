from django.urls import path
from movies.views import MovieCreateListView, MovieRetrieveDestroyAPIView

app_name='Movies'

urlpatterns = [
    path('', MovieCreateListView.as_view(), name='MovieCreateListView'),
    path('<int:pk>', MovieRetrieveDestroyAPIView.as_view(), name='MovieRetrieveDestroyAPIView'),
]