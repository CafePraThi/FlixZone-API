from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView

app_name='Genre'

urlpatterns = [
    path('', GenreCreateListView.as_view(), name='GenreCreateListView'),
    path('<int:pk>', GenreRetrieveUpdateDestroyView.as_view(), name='GenreRetrieveUpdateDestroyView'),
]