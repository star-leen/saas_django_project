from django.contrib import admin

# Register your models here.
from . import models

class SubscriptionPrice(admin.StackedInline):
    model = models.SubscriptionPrice
    readonly_fields = ['stripe_id']
    extra = 0
    can_delete = False

class SubscriptionAdmin(admin.ModelAdmin):
    inlines =[SubscriptionPrice]
    list_display = ['name', 'active']
    readonly_fields = ['stripe_id']


# admin.site.register(models.SubscriptionPrice)
admin.site.register(models.Subscription, SubscriptionAdmin)
admin.site.register(models.UserSubscription)