from rest_framework import serializers
from .models import LikeModel
from apps.user.models import UserModel
from apps.user.serializers import UserSerializer
from apps.post.models import PostModel
from apps.post.serializers import PostSerializer

class LikeSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=PostModel.objects.all())

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        representation['post'] = PostSerializer(instance.post).data

        if 'request' in self.context and self.context['request'].method == 'GET':
            representation.pop('post', None)  

        return representation

    class Meta:
        model = LikeModel
        extra_kwargs = {
            'user': {'read_only': True},
            'post': {'create_only': True},
        }
        fields = (
            'user',
            'post',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
