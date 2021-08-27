from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.http import response
from snacks.models import Snacks
import pytest


# Create your tests here.


class SnacksTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="tester", email="tester@email.com", password="pass")
        self.snack = Snacks.objects.create(name="Oreo", description="Good", purchaser=self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "Oreo")

    def test_home_page_status(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")

    def test_base_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "base.html")
