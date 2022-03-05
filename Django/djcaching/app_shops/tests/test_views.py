from django.test import TestCase
from app_shops.models import Shop, Product
from django.urls import reverse


class ShopListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_shops = 13
        for shop_num in range(number_of_shops):
            Shop.objects.create(name='Shop %s' % shop_num)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/shops/page_with_cached_fragments/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('page_with_cached_fragments'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'shops/page_with_cached_fragments.html')


class ProductListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        shop = Shop.objects.create(name='Shop')
        Product.objects.create(shop=shop, name='Apple', price=1)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/shops/product_list/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('product_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'shops/product_list.html')
