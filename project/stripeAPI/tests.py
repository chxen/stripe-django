from django.test import TestCase
from .models import Item

class ItemTests(TestCase):
    """Item model tests."""
	
    def test_str(self):
        item = Item(name='Test Item', description='Test Item Description', price=504)
        self.assertEquals(
            str(item),
            'Test Item',
        )