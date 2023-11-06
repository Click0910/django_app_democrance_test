from django.test import TestCase, Client
from django.urls import reverse
# from ..models import Policy


class PolicyViewTest(TestCase):

    def setUp(self):
        # Configure client for test
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/quotes/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('create-quote'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quote/quote_form.html')
