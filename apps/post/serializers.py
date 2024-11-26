from rest_framework import serializers
from .models import PostModel
from apps.user.models import UserModel
from apps.user.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())
    
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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        return representation