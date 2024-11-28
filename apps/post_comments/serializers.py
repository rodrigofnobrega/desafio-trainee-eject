from rest_framework import serializers
from .models import CommentModel
from apps.user.models import UserModel
from apps.user.serializers import UserSerializer
from apps.post.models import PostModel
from apps.post.serializers import PostSerializer

class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=PostModel.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())

    class Meta:
        model = CommentModel
        extra_kwargs = {
            'updated': {'read_only': True}
        }
        fields = (
            'id',
            'content',
            'created_at',
            'updated',
            'user',
            'post'
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        representation['post'] = PostSerializer(instance.post).data

        return representation