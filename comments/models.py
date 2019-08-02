from django.db import models
from blogs.models import BlogPost
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    """Model of a comment"""
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of the model"""
        return self.text