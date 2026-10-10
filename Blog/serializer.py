from rest_framework import serializers
from .models import Blogs, Category, Comment, Tags

class BlogsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Blogs
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CoommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = '__all__'

