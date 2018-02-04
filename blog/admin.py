from django.contrib import admin

# Register your models here.
# Intialise Admin for model Post

from .models import Post

admin.site.register(Post)

