from django.shortcuts import render

from .models import Post
from django.utils import timezone


# Get all posts which are published using orm

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now())
	return render(request, 'blog/post_list.html', {'posts':posts})
