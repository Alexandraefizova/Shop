from django.contrib import admin
from .models import Coupon


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']


admin.site.register(Coupon, CouponAdmin)
