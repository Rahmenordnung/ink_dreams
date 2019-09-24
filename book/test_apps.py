from django.apps import apps
from django.test import TestCase
from .apps import BookConfig


class TestBookConfig(TestCase):

    def test_book_app(self):
        self.assertEqual("book", BookConfig.name)
        self.assertEqual("book", apps.get_app_config("book").name)