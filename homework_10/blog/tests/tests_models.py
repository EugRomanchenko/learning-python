from django.test import TestCase

from blog.models import User, Post


class PostTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(name="Jhon", username="Jhon", email="jhon@example.com")
        self.post = Post.objects.create(title="Some new post", body="Hello there", user=self.user)

    def tearDown(self):
        User.objects.all().delete()
        Post.objects.all().delete()

    def test_str(self):
        self.assertEqual(str(self.post.title), "Some new post")


class UserTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(name="Dan", username="Dan", email="dan@yahoo.com")

    def tearDown(self):
        User.objects.all().delete()

    def test_str(self):
        self.assertEqual(str(self.user.name), "Dan")
