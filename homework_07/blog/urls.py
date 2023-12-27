from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path(
        "",
        views.posts_view,
        name="index",
    ),
    path(
        "users/",
        views.users_with_posts,
        name="users-with-posts",
    ),
]
