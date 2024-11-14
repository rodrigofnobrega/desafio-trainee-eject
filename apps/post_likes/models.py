from django.db import models
from uuid import uuid4
from apps.user.models import UserModel
from apps.post.models import PostModel

# Create your models here.
class LikeModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, related_name="likes", on_delete=models.CASCADE)
