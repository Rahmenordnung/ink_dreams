from django.test import TestCase

# pages/tests.py
from django.http import HttpRequest

from django.urls import reverse

# Create your tests here.

class HomePageTests(TestCase):
  
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        
    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h2>Some books</h2>')    