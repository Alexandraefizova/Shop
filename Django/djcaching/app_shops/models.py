
from django.db import models
from django.utils.translation import gettext_lazy as _
from coupons.models import Coupon
from app_users.models import User


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))


class Product(models.Model):
    shop = models.ForeignKey(Shop, related_name='shop', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name=_('product'))
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('price'))

    class Meta:
        verbose_name_plural = _('products')
        verbose_name = _('product')


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=300, verbose_name=_('balance'))
    coupon = models.ManyToManyField(Coupon)

