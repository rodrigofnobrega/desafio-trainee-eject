from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import LikeModel
from .serializers import LikeSerializer

# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer


    @swagger_auto_schema(
        operation_description="Obter todos os likes",
        responses={
            200: LikeSerializer(many=True),
            401: "Unauthorized - Token JWT inválido ou ausente"
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Adicionar um novo like para um post",
        responses={
            200: LikeSerializer(many=True),
            401: "Unauthorized - Token JWT inválido ou ausente"
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obter todas as curtidas de um post pelo post id",
        responses={
            200: LikeSerializer(many=True),
            401: "Unauthorized - Token JWT inválido ou ausente",
            404: "Not Found - Comentário não encontrado"
        },
        manual_parameters=[
            openapi.Parameter(
                'post_id', 
                openapi.IN_PATH, 
                description="ID do post", 
                type=openapi.TYPE_STRING, 
                required=True
            ),
        ]
    )
    @action(detail=False, methods=['get'], url_path='post/(?P<post_id>[^/.]+)')
    def likes_by_post(self, request, post_id=None):
        comments = LikeModel.objects.filter(post_id=post_id)  

        paginator = PageNumberPagination()
        paginator.page_size = self.request.query_params.get('PAGE_SIZE', settings.PAGE_SIZE)
        paginated_comments = paginator.paginate_queryset(comments, request)
        
        serializer = self.get_serializer(paginated_comments, many=True)
        
        return paginator.get_paginated_response(serializer.data)


    @swagger_auto_schema(
        operation_description="Obter todas as curtidas de um usuário pelo usuário id",
        responses={
            200: LikeSerializer(many=True),
            401: "Unauthorized - Token JWT inválido ou ausente",
            404: "Not Found - Comentário não encontrado"
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
    def comments_by_post(self, request, user_id=None):
        comments = LikeModel.objects.filter(user_id=user_id)  

        paginator = PageNumberPagination()
        paginator.page_size = self.request.query_params.get('PAGE_SIZE', settings.PAGE_SIZE)
        paginated_comments = paginator.paginate_queryset(comments, request)
        
        serializer = self.get_serializer(paginated_comments, many=True)
        
        return paginator.get_paginated_response(serializer.data)