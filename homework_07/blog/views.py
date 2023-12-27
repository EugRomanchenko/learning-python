from django.http import HttpRequest
from django.shortcuts import render

from .models import User, Post


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
