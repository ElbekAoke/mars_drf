from .views import PostAPIView, PostCreateAPIView, PostDetailAPIView
from django.urls import path


urlpatterns = [
    path('', PostAPIView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:id>/', PostDetailAPIView.as_view(), name='detail'),
]
