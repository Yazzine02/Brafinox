from django.test import TestCase
from .models import Client, Product, Sell, BL

# Create your tests here.
class ModelTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(first_name='John', last_name='Doe')
        self.product = Product.objects.create(name='Product A', description='Test product', stock_unit=100)
        self.bl = BL.objects.create(client=self.client)
    
    def test_sell(self):
        sell = Sell.objects.create(client=self.client, product=self.product, bl=self.bl, quantity=2, sell_price=50)
        self.assertEqual(sell.total_price, 100)
    def test_bl_total_amount(self):
        Sell.objects.create(client=self.client, product=self.product, bl=self.bl, quantity=2, sell_price=50)
        Sell.objects.create(client=self.client, product=self.product, bl=self.bl, quantity=1, sell_price=50)
        self.assertEqual(self.bl.total_amount, 150)