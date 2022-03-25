from email.policy import default
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
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    updated =models.DateTimeField(auto_now=True)
    
   
    def __str__(self):
        return self.ekko

    class Meta:
        ordering = ['-created_at']

    @property
    def num_likes(self):
        return self.like.all().count()

class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    comment = models.TextField(max_length=500, default='comment')
    ekko = models.ForeignKey(Ekko, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.title

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ekko = models.ForeignKey(Ekko, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.ekko)