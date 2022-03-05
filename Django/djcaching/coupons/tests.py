# from django.test import TestCase
# from coupons.models import Coupon
#
#
# class CouponModelTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         Coupon.objects.create(code='1234', valid_from='2021-02-01', valid_to='2021-01-01', discount=10)
#
#     def test_first_name_label(self):
#         coupon = Coupon.objects.get(id=1)
#         max_length = coupon._meta.get_field('code').max_length
#         self.assertEquals(max_length, 50)

