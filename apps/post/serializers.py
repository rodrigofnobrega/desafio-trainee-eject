from rest_framework import serializers
from .models import PostModel
from apps.user.models import UserModel
from apps.user.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = PostModel
        extra_kwargs = {
            'publication_date': {'read_only': True},
            'updated': {'read_only': True}
        }
        fields = (
            'id',
            'title',
            'content',
            'total_likes',
            'updated',
            'publication_date',
            'image',
            'video',
            'user',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        return representation
    
    def get_total_likes(self, obj):
        return obj.likes.count()
    
    def update(self, instance, validated_data):
        validated_data['updated'] = True
        return super().update(instance, validated_data)