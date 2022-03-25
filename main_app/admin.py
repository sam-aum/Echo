from django.contrib import admin
from .models import Ekko, Comment, Like

# Register your models here.
admin.site.register(Ekko)
admin.site.register(Comment)
admin.site.register(Like)

