from rest_framework import serializers
from .models import UserModel
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        extra_kwargs = {
            'password': {'write_only': True}
        }
        fields = (
            'id',
            'name', 
            'email', 
            'password', 
            'created_at'
        )

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password']) 
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)
        
