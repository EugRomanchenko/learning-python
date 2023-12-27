from django.db import models


class User(models.Model):
    class Meta:
        verbose_name_plural = "Users"

    name = models.CharField(max_length=64, unique=True)
    username = models.CharField(max_length=64, unique=True)
    email = models.CharField(max_length=64, unique=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name_plural = "Post"

    title = models.CharField(max_length=100, default="", null=False)
    body = models.TextField(max_length=200, default="", null=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
    )

    def __str__(self):
        return self.title
