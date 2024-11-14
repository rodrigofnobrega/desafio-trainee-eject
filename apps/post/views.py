from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PostModel
from .serializers import PostSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
