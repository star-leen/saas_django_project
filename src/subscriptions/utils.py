from django.db.models import Q
import helpers.billing
from customers.models import Customer
from subscriptions.models import UserSubscription, Subscription, SubscriptionStatus

def refresh_active_users_subscriptions(
    user_ids=None,
    active_only=True,
    days_ago=0,
    days_left=0,
    day_start=0,
    day_end=0,
    verbose=False):
    qs = UserSubscription.objects.all()
    if active_only:
        qs = qs.by_active_trialing()
        print("qs: ", qs)
    if user_ids is not None:
        qs = qs.by_user_ids(user_ids=user_ids)
    if days_ago > 0:
        qs = qs.by_days_ago(days_ago=days_ago)
    if days_left > 0:
        qs = qs.by_days_left(days_left=days_left)
    if day_start > 0 and day_end > 0:
        qs = qs.by_range(day_start=day_start, day_end=day_end)

    complete_count = 0
    qs_count = qs.count()
    print(qs_count)
    for obj in qs:
        if verbose:
            print("Updating user", obj.user, obj.subscription, obj.current_period_end)
        if obj.stripe_id:
            sub_data = helpers.billing.get_subscription(obj.stripe_id, raw=False)
            for k,v in sub_data.items():
                setattr(obj, k, v)
            obj.save()
            complete_count += 1
    return complete_count == qs_count

def clear_dangling_subs():
    qs = Customer.objects.filter(stripe_id__isnull=False)
    for customer_obj in qs:
        user = customer_obj.user
        customer_stripe_id = customer_obj.stripe_id
        print(f'Sync {user} - {customer_stripe_id} subs and remove old ones')
        subs = helpers.billing.get_customer_active_subscriptions(customer_stripe_id=customer_obj)
        for sub in subs:
            existing_user_subs_qs = UserSubscription.objects.filter(stripe_id__iexact=f"{sub.id}".strip())
            if existing_user_subs_qs.exists:
                continue
            helpers.billing.cancel_subscription(stripe_id=sub.id, reason="Dangling Active Subscription", cancel_at_period_end=True)
            print(sub.id, existing_user_subs_qs.exists())
        
def sync_subs_groups_permissions():
    qs = Subscription.objects.filter(active=True)
    for obj in qs:
        sub_perms = obj.permissions.all()
        for group in obj.groups.all():
            group.permissions.set(sub_perms)