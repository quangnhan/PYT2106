from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class BlogTest(TestCase):
    def test_blog_list_view(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
