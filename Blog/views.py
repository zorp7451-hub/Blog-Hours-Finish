from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import viewsets,serializers
from .serializer import BlogsSerializer,CoommentSerializer,TagSerializer,CategorySerializer
from .models import Blogs,Tags,Comment,Category
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from django.shortcuts import get_object_or_404
from .pagination import BlogPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = BlogPagination
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'status']
    search_fields = ['title', 'text']
    ordering_fields = ['created_at']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Blogs.objects.all()
        return Blogs.objects.filter(status='published')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        blog = self.get_object()
        if blog.user == self.request.user and blog.status not in ['draft', 'rejected']:
            raise serializers.ValidationError("Редактировать можно только черновики или отклоненные статьи!")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user == self.request.user and instance.status not in ['draft', 'rejected']:
            raise serializers.ValidationError("Удалять можно только черновики или отклоненные статьи!")
        instance.delete()


    @action(detail=True, methods=['post'])
    def send_review(self, request, pk=None):
        blog = self.get_object()
        blog.status = 'under_review'
        blog.save()
        return Response({'message': 'Статья отправлена на проверку'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def moderate(self, request, pk=None):
        blog = self.get_object()
        action_type = request.data.get('action')

        if action_type == 'approve':
            blog.status = 'published'
            blog.save()
            return Response({'message': 'Статья одобрена и опубликована'}, status=status.HTTP_200_OK)
        elif action_type == 'reject':
            blog.status = 'rejected'
            blog.save()
            return Response({'message': 'Статья отклонена'}, status=status.HTTP_200_OK)

        return Response({'error': 'Укажите action: approve или reject'}, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CoommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)