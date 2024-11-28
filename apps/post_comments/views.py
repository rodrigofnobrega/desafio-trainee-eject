from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from .models import CommentModel
from .serializers import CommentSerializer

# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    @action(detail=False, methods=['get'], url_path='post/(?P<post_id>[^/.]+)')
    def comments_by_post(self, request, post_id=None):
        comments = CommentModel.objects.filter(post_id=post_id)  

        paginator = PageNumberPagination()
        paginator.page_size = self.request.query_params.get('PAGE_SIZE', settings.PAGE_SIZE)
        paginated_comments = paginator.paginate_queryset(comments, request)
        
        serializer = self.get_serializer(paginated_comments, many=True)
        
        return paginator.get_paginated_response(serializer.data)