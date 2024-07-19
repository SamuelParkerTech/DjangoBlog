from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "DRAFT"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title =models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    auithor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

status = models.IntegerField(choices=STATUS, default=0)