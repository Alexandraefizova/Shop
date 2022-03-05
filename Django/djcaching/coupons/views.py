from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Coupon
from .forms import CouponApplyForm
from django.core.cache import cache


@require_POST
def coupon_apply(request):
    username = request.user.username
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            coupon_cache_key = 'coupon:{}'.format(username)
            cache.get_or_set(coupon_cache_key, coupon, 30*60)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExists:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')
