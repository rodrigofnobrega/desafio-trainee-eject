from rest_framework import serializers
from .models import CommentModel
from apps.user.models import UserModel
from apps.user.serializers import UserSerializer
from apps.post.models import PostModel
from apps.post.serializers import PostSerializer

class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=PostModel.objects.all())

    class Meta:
        model = CommentModel
        extra_kwargs = {
            'updated': {'read_only': True},
            'user': {'read_only': True},
        }
        fields = (
            'id',
            'content',
            'created_at',
            'updated',
            'image',
            'video',
            'user',
            'post'
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        representation['post'] = PostSerializer(instance.post).data

        return representation
    
    def update(self, instance, validated_data):
        validated_data['updated'] = True
        return super().update(instance, validated_data)
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)