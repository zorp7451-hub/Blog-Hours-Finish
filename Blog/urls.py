from django.contrib import admin
from .views import *
from django.urls import path


urlpatterns = [
    path('blogs/', BlogViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('blogs/<int:pk>/', BlogViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('blogs/<int:pk>/send-review/', BlogViewSet.as_view({'post': 'send_review'})),
    path('blogs/<int:pk>/moderate/', BlogViewSet.as_view({'post': 'moderate'})),
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
]