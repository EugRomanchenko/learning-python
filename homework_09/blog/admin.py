from django.contrib import admin
from .models import User, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = "id", "title", "body", "user"
    list_display_links = "id", "title"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = "id", "name", "username", "email"
    list_display_links = "id", "name", "username"
