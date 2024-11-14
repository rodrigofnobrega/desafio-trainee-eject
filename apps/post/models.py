from django.db import models
from django.utils import timezone
from uuid import uuid4
from apps.user.models import UserModel 

# Create your models here.
class PostModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)
    updated = models.BooleanField(default=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
