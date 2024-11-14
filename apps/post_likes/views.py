from rest_framework import viewsets
from .models import LikeModel
from .serializers import LikeSerializer

# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer