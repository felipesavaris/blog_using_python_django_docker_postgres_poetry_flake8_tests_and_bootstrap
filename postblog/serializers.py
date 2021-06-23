from rest_framework import serializers

from .models import PostBlog


class PostBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostBlog
        fields = '__all__'
