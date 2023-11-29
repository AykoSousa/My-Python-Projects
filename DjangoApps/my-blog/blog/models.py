from turtle import title
from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['create_on']
    
    def __str__(self):
        return self.title