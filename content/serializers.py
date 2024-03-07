from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post, PostMedia, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = (
            'id',
            'media_type',
            'media_file',
        )


class PostSerializer(serializers.ModelSerializer):
    account = UserSerializer(read_only=True)
    media = MediaSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'caption',
            'comments',
            'account',
            'media',
            'mentions',
        )


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'post',
            'content',
            'created_date',
            'updated_date',
        )
