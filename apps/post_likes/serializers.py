from rest_framework import serializers
from .models import LikeModel
from apps.user.models import UserModel
from apps.user.serializers import UserSerializer
from apps.post.models import PostModel
from apps.post.serializers import PostSerializer

class LikeSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=PostModel.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        representation['post'] = PostSerializer(instance.post).data

        return representation

    class Meta:
        model = LikeModel
        fields = (
            'user',
            'post',
        )
