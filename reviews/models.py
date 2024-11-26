from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Review(models.Model):
    """
    null = True if users want to stay anonymous
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_posts", null=True, blank=True)
    RATING_CHOICES = [(i, str(i)) for i in range(6)]
    rating = models.IntegerField(choices=RATING_CHOICES)
    content = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    