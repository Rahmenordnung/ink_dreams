from django.test import TestCase
from .models import Book
from django.contrib.auth.models import User


class TestBookModel(TestCase):

    def test_create_Book(self):
        book = Book(title='Test Book',
                          description='Some book content.')
        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.description, "Some book content.")
        self.assertFalse(book.cover)
        self.assertFalse(book.price)
        
    # def test_title_max_length(self):
    #     book = Book.objects.get(id=1)
    #     max_length = book._meta.get_field('title').max_length
    #     self.assertEquals(max_length, 100)    