from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse

from book.models import Book

# Create your tests here.

class HomePageTests(TestCase):
  
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        
        
    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>Books list</title>')
        
        
        
    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'I am so lost!')
        
    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
                    
class book_detail_viewTests(TestCase):
  
    def test_book_detail_view(self):
        obj = self.client.get(title='book_detail', path='book_detail/<slug>/')
        response = self.client.get('book_detail/<slug>/')
        self.assertEqual(response.status_code, 404) 
      
class order_final_viewTests(TestCase):
  
    def test_detail_view(self):
        obj = self.client.get(title='Order Summary', path='order_final_view/')
        response = self.client.get('order_final_view/slug/')
        self.assertEqual(response.status_code, 404)
        
        
        
        
                               