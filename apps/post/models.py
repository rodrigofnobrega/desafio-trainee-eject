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
    image = models.ImageField(upload_to='post_images/', null=True, blank=True) 
    video = models.FileField(upload_to='post_videos/', null=True, blank=True) 
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f"{self.title} | {self.user}"
