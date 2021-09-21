from django.test import TestCase
from django.urls import reverse
from .models import Blog
# Create your tests here.

class BlogTest(TestCase):
    def Setup(self):
        Blog.objects.create(name="Blog1")
        Blog.objects.create(name="Blog2")

    def test_blog_list_view(self):
        print("[Debugging...]"), reverse('blog_list')
        response = self.client.get(reverse('blog_List'))
        list_all_blog = response.context_data['list_all_blog']

        self.assertEqual(list_all_blog.count(), 2)
        self.assertEqual(response.status_code, 200)

    def test_blog_create_view(self):
        response = self.client.get(reverse('blog_create'))
        self.assertEqual(response.status_code, 200)

    def test_blog_create_post(self):
        data = {'name': "blog"}
        response = self.client.post(reverse('blog_post_create'), data)
        print(response)
        self.assertEqual(response.status_code, 200)
        list_all_blog = Blog.objects.all()
        print(list_all_blog)
        self.assertEqual(list_all_blog.count(), 3)