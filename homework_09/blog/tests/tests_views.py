from django.test import TestCase

from blog.models import User, Post


class PostListViewTestCase(TestCase):

    def setUp(self):
        self.url = "/blog/list/"

    def tearDown(self):
        User.objects.all().delete()
        Post.objects.all().delete()

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        response = self.client.get(self.url)
        context = response.context
        self.assertIn("posts", context)
        posts = context["posts"]
        self.assertEqual(len(posts), 0)
        user = User.objects.create(name="Jhon", username="Jhon", email="jhon@example.com")
        post = Post.objects.create(title="Some new post", body="Hello there", user=user)
        response = self.client.get(self.url)
        context = response.context
        posts = context["posts"]
        self.assertEqual(len(posts), 1)
