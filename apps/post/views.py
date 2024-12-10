from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from .models import PostModel
from .serializers import PostSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

    @swagger_auto_schema(
        operation_description="Obter todos os posts",
        responses={
            200: PostSerializer(many=True),
            401: "Unauthorized - Token JWT inválido ou ausente"
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Criar um novo post",
        responses={
            200: PostSerializer(many=True),
            401: "Unauthorized - Token JWT inválido ou ausente"
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Lista os posts de um usuário pelo ID",
        responses={
            200: PostSerializer(many=True),
            401: "Unauthorized - Token JWT inválido ou ausente",
            404: "Not Found - Usuário não encontrado"
        },
        manual_parameters=[
            openapi.Parameter(
                'user_id', 
                openapi.IN_PATH, 
                description="ID do usuário", 
                type=openapi.TYPE_STRING, 
                required=True
            ),
        ]
    )
    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)')
    def posts_by_user(self, request, user_id=None):
        posts = PostModel.objects.filter(user_id=user_id)  

        paginator = PageNumberPagination()
        paginator.page_size = self.request.query_params.get('PAGE_SIZE', settings.PAGE_SIZE)
        paginated_comments = paginator.paginate_queryset(posts, request)
        
        serializer = self.get_serializer(paginated_comments, many=True)

        return paginator.get_paginated_response(serializer.data)