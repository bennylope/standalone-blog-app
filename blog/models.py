from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="blog_posts",
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=100)
    body = models.TextField()
