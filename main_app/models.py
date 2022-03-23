from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Ekko(models.Model):

    # name = models.CharField(max_length=100)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    ekko = models.TextField(max_length=500)
    source = models.CharField(max_length=250, default='anonymous')
    verified_ekko = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # like = models.ManyToManyField(User, related_name='likes')
   

    def __str__(self):
        return self.ekko

    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    comment = models.TextField(max_length=500, default='comment')
    ekko = models.ForeignKey(Ekko, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.title