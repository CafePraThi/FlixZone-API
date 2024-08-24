from django.urls import path
from . import views

app_name='Genre'

urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view(), name='GenreCreateListView'),
    path('genres/<int:pk>', views.GenreRetrieveUpdateDestroyView.as_view(), name='GenreRetrieveUpdateDestroyView'),
]