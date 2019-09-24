from django.apps import apps
from django.test import TestCase
from .apps import ProfilesConfig


class TestProfilesConfig(TestCase):

    def test_profiles_app(self):
        self.assertEqual("profiles", ProfilesConfig.name)
        self.assertEqual("profiles", apps.get_app_config("profiles").name)