from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CommentModel
from .serializers import CommentSerializer

# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    @action(detail=False, methods=['get'], url_path='post/(?P<post_id>[^/.]+)')
    def comments_by_post(self, request, post_id=None):
        comments = CommentModel.objects.filter(post_id=post_id)  
        serializer = self.get_serializer(comments, many=True)

        return Response(serializer.data)