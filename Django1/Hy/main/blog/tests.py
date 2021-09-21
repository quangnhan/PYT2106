from django.test import TestCase
from django.urls import reverse
from .models import Blog
# Create your tests here.
class BlogTest(TestCase):
    def setUp(self):
        Blog.objects.create(name="blog1")
        Blog.objects.create(name="blog2")
        Blog.objects.create(name="blog3")

    def test_blog_list_view(self):
        response = self.client.get(reverse('blog_list'))
        list_all_blog = response.context_data['list_all_blog']
        self.assertEqual(list_all_blog.count(), 3)
        self.assertEqual(response.status_code, 200)

    def test_blog_create_view(self):
        response = self.client.get(reverse('blog_create'))
        self.assertEqual(response.status_code, 200)
        
    def test_blog_create_post(self):
        data = {'name':'blog'}
        response = self.client.post(reverse('blog_post_create'), data)
        self.assertEqual(response.status_code, 200)
        list_all_blog = Blog.objects.all()
        self.assertEqual(list_all_blog.count(),4)