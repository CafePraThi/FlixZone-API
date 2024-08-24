from django.urls import path
from reviews.views import ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView

app_name='Reviews'

urlpatterns = [
    path('reviews/', ReviewListCreateAPIView.as_view(), name='ReviewListCreateAPIView'),
    path('reviews/<int:pk>', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='ReviewRetrieveUpdateDestroyAPIView'),
]