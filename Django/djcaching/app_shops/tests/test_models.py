from django.test import TestCase
from app_shops.models import Shop, Product


class ShopModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Shop.objects.create(name='Shop')

    def test_name_label(self):
        shop = Shop.objects.get(id=1)
        field_label = shop._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        shop = Shop.objects.get(id=1)
        max_length = Shop._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        shop = Shop.objects.create(name='Shop')
        Product.objects.create(shop=shop, name='Apple', price=1)

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'product')

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')