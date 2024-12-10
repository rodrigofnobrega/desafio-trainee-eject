from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import CommentModel
from .serializers import CommentSerializer

# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    @swagger_auto_schema(
        operation_description="Obter todos os comentários",
        responses={
            200: CommentSerializer(many=True),
            401: "Unauthorized - Token JWT inválido ou ausente"
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Criar um novo comentário para um post",
        responses={
            200: CommentSerializer(many=True),
            401: "Unauthorized - Token JWT inválido ou ausente"
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obter todos os comentários de um post pelo post id",
        responses={
            200: CommentSerializer(many=True),
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
    def comments_by_post(self, request, post_id=None):
        comments = CommentModel.objects.filter(post_id=post_id)  

        paginator = PageNumberPagination()
        paginator.page_size = self.request.query_params.get('PAGE_SIZE', settings.PAGE_SIZE)
        paginated_comments = paginator.paginate_queryset(comments, request)
        
        serializer = self.get_serializer(paginated_comments, many=True)
        
        return paginator.get_paginated_response(serializer.data)