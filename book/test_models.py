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