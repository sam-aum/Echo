from django.db import models
# from django.

# Create your models here.
class Ekko(models.Model):

    # name = models.CharField(max_length=100)
    user = models.CharField(max_length=100, default='sam-aum')
    ekko = models.TextField(max_length=500)
    source = models.CharField(max_length=250, default='anonymous')
    verified_ekko = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ekko

    class Meta:
        ordering = ['-created_at']