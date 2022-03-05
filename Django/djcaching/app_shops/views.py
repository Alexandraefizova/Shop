from django.core.cache import cache
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from app_shops.models import Shop, Product, UserAccount
from app_shops.forms import UserAccountForm
from django.views import View
from app_users.models import User


def page_with_cached_fragments(request):
    shops = Shop.objects.all()
    return render(request, 'shops/page_with_cached_fragments.html', context={
        'shops': shops
    })


def product_list(request):
    product = Product.objects.all()
    return render(request, 'shops/product_list.html', {'product': product})


class AccountFormView(View):

    def get(self, request):
        form = UserAccountForm
        return render(request, 'shops/account.html', context={'form': form})

    def post(self, request):
        form = UserAccountForm(request.POST)

        if form.is_valid():
            balance = form.cleaned_data['balance']
            coupon = form.cleaned_data['coupon']
            return HttpResponseRedirect('/')
        return render(request, 'shops/account.html', context={'form': form})


