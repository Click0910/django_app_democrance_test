from django.test import TestCase
from customers.models import Customer


class CustomerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Configure a test object
        Customer.objects.create(first_name='John', last_name='Doe', dob='1990-01-01')

    def test_first_name_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_date_of_birth(self):
        customer = Customer.objects.get(id=1)
        self.assertEqual(customer.dob.strftime('%Y-%m-%d'), '1990-01-01')

    def test_str_method(self):
        customer = Customer.objects.get(id=1)
        expected_object_name = f'{customer.first_name} {customer.last_name}'
        self.assertEqual(str(customer), expected_object_name)
