from django.shortcuts import render, redirect

from .models import PostBlog
from postblog.form import PostBlogForms


def list_all_posts(request):
    posts = PostBlog.objects.all()
    return render(request, 'list_all_posts.html', {'posts': posts})


def create_post(request):
    form = PostBlogForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_all_posts')
    return render(request, 'form.html', {'form': form})


def update_post(request, id):
    post = PostBlog.objects.get(id=id)
    form = PostBlogForms(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('list_all_posts')
    return render(request, 'form.html', {'form': form})


def delete_post(request):
    pass
