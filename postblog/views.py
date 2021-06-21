from django.shortcuts import render

from .models import PostBlog


def list_all_posts(request):
    posts = PostBlog.objects.all()
    return render(request, 'list_all_posts.html', {'posts': posts})


def update_post(request):
    pass


def delete_post(request):
    pass
