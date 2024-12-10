from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from .models import LikeModel
from .serializers import LikeSerializer

# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer

    @action(detail=False, methods=['get'], url_path='post/(?P<post_id>[^/.]+)')
    def likes_by_post(self, request, post_id=None):
        comments = LikeModel.objects.filter(post_id=post_id)  

        paginator = PageNumberPagination()
        paginator.page_size = self.request.query_params.get('PAGE_SIZE', settings.PAGE_SIZE)
        paginated_comments = paginator.paginate_queryset(comments, request)
        
        serializer = self.get_serializer(paginated_comments, many=True)
        
        return paginator.get_paginated_response(serializer.data)

    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)')
    def comments_by_post(self, request, user_id=None):
        comments = LikeModel.objects.filter(user_id=user_id)  

        paginator = PageNumberPagination()
        paginator.page_size = self.request.query_params.get('PAGE_SIZE', settings.PAGE_SIZE)
        paginated_comments = paginator.paginate_queryset(comments, request)
        
        serializer = self.get_serializer(paginated_comments, many=True)
        
        return paginator.get_paginated_response(serializer.data)