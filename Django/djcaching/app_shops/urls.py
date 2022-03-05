from django.urls import path
from app_shops.views import page_with_cached_fragments, product_list, AccountFormView


urlpatterns = [
    path('page_with_cached_fragments/', page_with_cached_fragments, name='page_with_cached_fragments'),
    path('product_list/', product_list, name='product_list'),
    path('account/', AccountFormView.as_view(), name='user_account'),
]
