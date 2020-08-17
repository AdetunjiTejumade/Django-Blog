from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Blog
# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Blog.objects.create(
            title='A good title',
            body= 'A normal body',
        )
    def test_string_representation(self):
        post = Blog(title='A good title')
        self.assertEqual(str(post), post.title)


    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(),'/1/')
