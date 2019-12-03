from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    blog_posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": blog_posts})


def post_detail(request, post_id):
    blog_post = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/post_detail.html", {"post": blog_post})
