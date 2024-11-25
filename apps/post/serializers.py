from rest_framework import serializers
from .models import PostModel
from apps.user.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = PostModel
        fields = (
            'id',
            'title',
            'content',
            'publication_date',
            'user',
        )