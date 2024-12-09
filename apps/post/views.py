from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from .models import PostModel
from .serializers import PostSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

    # Endpoint para obter todos os posts de um usuário pelo ID do usuário.
    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)')
    def posts_by_user(self, request, user_id=None):
        posts = PostModel.objects.filter(user_id=user_id)  

        paginator = PageNumberPagination()
        paginator.page_size = self.request.query_params.get('PAGE_SIZE', settings.PAGE_SIZE)
        paginated_comments = paginator.paginate_queryset(posts, request)
        
        serializer = self.get_serializer(paginated_comments, many=True)

        return paginator.get_paginated_response(serializer.data)