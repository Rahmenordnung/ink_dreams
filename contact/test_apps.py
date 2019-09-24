from django.apps import apps
from django.test import TestCase
from .apps import ContactFormConfig


class TestContactFormConfig(TestCase):

    def test_contact_app(self):
        self.assertEqual("contact", ContactFormConfig.name)
        self.assertEqual("contact", apps.get_app_config("contact").name)