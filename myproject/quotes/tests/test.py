from django.test import TestCase
from django.contrib.auth.models import User
from quotes.models import Policy
from customers.models import Customer


class PolicyModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Configure objects for test
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_customer = Customer.objects.create(first_name='Jane', last_name='Doe', dob='1995-05-15')
        Policy.objects.create(type='Basic', premium=100.00, cover=5000.00, customer=test_customer)

    def test_policy_creation(self):
        policy = Policy.objects.get(id=1)
        self.assertTrue(isinstance(policy, Policy))
        self.assertEqual(policy.type, 'Basic')

    def test_policy_association_with_customer(self):
        policy = Policy.objects.get(id=1)
        self.assertEqual(policy.customer.first_name, 'Jane')
