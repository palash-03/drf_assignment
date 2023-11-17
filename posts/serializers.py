from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Posts

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Posts
        fields = ['id', 'title', 'body', 'author']