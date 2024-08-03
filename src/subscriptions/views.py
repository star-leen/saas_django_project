from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
import helpers.billing
from .models import SubscriptionPrice, UserSubscription
from . import utils as subs_utils


# Create your views here.
@login_required
def user_subscription_view(request):
    user_sub_obj, created = UserSubscription.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        finished = subs_utils.refresh_active_users_subscriptions(user_ids=[request.user.id], active_only=False)
        if finished:
            messages.success(request, "Your details have been refreshed.")
        else:
            messages.error(request, "Your details have not been refreshed, please try again.")
        return redirect(user_sub_obj.get_absolute_url())
    
    context = {
        "subscription": user_sub_obj,
    }
    return render(request, 'subscriptions/user_detail_view.html', context)


@login_required
def user_subscription_cancel_view(request):
    user_sub_obj, created = UserSubscription.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        if user_sub_obj.stripe_id and user_sub_obj.is_active_status:
            sub_data = helpers.billing.cancel_subscription(
                user_sub_obj.stripe_id,
                reason="User wanted to end",
                feedback="other",
                cancel_at_period_end=True,
                raw=False)
            for k,v in sub_data.items():
                setattr(user_sub_obj, k, v)
            user_sub_obj.save()
            messages.success(request, "Your plan has been cancelled")
        return redirect(user_sub_obj.get_absolute_url())
    
    context = {
        "subscription": user_sub_obj,
    }
    return render(request, 'subscriptions/user_cancel_view.html', context)


def subscription_price_view(request, interval='month'):
    qs = SubscriptionPrice.objects.filter(featured=True)
    intv_mo = SubscriptionPrice.IntervalChoices.MONTHLY
    intv_yr = SubscriptionPrice.IntervalChoices.YEARLY
    object_list = qs.filter(interval=intv_mo)
    url_path_name = 'pricing-interval'
    mo_url = reverse(url_path_name, kwargs={'interval': intv_mo})
    yr_url = reverse(url_path_name, kwargs={'interval': intv_yr})
    active = intv_mo
    if interval == intv_yr:
        active = intv_yr
        object_list = qs.filter(interval=intv_yr)
    context = {
        'object_list':object_list,
        'mo_url': mo_url,
        'yr_url': yr_url,
        'active': active,
        }
    return render(request, 'subscriptions/pricing.html', context)