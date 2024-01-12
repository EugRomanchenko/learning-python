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
    path(
        "list/",
        views.PostListView.as_view(),
        name="list"
    ),
    path(
        "detail/<int:pk>/",
        views.PostDetailView.as_view(),
        name="detail"
    ),
    path(
        "create/",
        views.PostCreateView.as_view(),
        name="create"
    ),
]
