from django.db import models
from uuid import uuid4
from apps.user.models import UserModel
from apps.post.models import PostModel

# Create your models here.
class CommentModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.BooleanField(default=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, related_name="comments", on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.content} | {self.user} | {self.post}"

