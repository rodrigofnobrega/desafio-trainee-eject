from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import PostModel
from .serializers import PostSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

    # Endpoint para obter todos os posts de um usuário pelo ID do usuário.
    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)')
    def posts_by_user(self, request, user_id=None):
        print(user_id)
        posts = PostModel.objects.filter(user_id=user_id)  
        serializer = self.get_serializer(posts, many=True)

        return Response(serializer.data)