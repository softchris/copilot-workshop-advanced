import unittest

from app import apply_discount

class TestApplyDiscount(unittest.TestCase):
    def test_apply_discount(self):
        cart = [
            {'id': 1, 'name': 'Product 1', 'price': 10.0},
            {'id': 2, 'name': 'Product 2', 'price': 20.0},
            {'id': 3, 'name': 'Product 3', 'price': 30.0},
            {'id': 4, 'name': 'Product 4', 'price': 40.0},
            {'id': 5, 'name': 'Product 5', 'price': 50.0}
        ]
        self.assertEqual(apply_discount(cart), 140.0) # i.e the cheapest one, 10.0 should be free, total without discount is 150.0