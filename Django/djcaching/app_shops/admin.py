from django.contrib import admin
from app_shops.models import Shop, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


admin.site.register(Product, ProductAdmin)


class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Shop, ShopAdmin)


