from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .models import UserModel
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    @swagger_auto_schema(
        operation_description="Obter todos os usuários",
        responses={
            200: UserSerializer(many=True),
            401: "Unauthorized - Token JWT inválido ou ausente"
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Criar um novo usuário",
        responses={
            200: UserSerializer(many=True)
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
