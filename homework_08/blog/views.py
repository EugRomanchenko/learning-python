from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import User, Post
from .forms import PostForm


def posts_view(request: HttpRequest):
    posts = (
        Post
        .objects
        .select_related("user")
        .all()
    )
    context = {
        "posts": posts,
    }
    return render(
        request,
        "posts/posts-list.html",
        context,
    )


def users_with_posts(request: HttpRequest):
    context = {
        "users": (
            User
            .objects
            .prefetch_related("posts")
            .all()
        )
    }
    return render(
        request,
        "posts/users-with-posts.html",
        context,
    )


class PostListView(ListView):
    models = Post
    template_name = "posts/post-list.html"

    def get_queryset(self):
        return Post.objects.select_related("user").all()


class PostDetailView(DetailView):
    models = Post
    template_name = "posts/post-detail.html"

    def get_queryset(self):
        return Post.objects.select_related("user").all()


class PostCreateView(CreateView):
    models = Post
    template_name = "posts/post-create.html"
    form_class = PostForm
    success_url = reverse_lazy("blog:list")
