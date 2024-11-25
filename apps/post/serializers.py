from rest_framework import serializers
from .models import PostModel
from apps.user.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer
    
    class Meta:
        model = PostModel
        extra_kwargs = {
            'publication_date': {'read_only': True}
        }
        fields = (
            'id',
            'title',
            'content',
            'publication_date',
            'user',
        )