from django.urls import path
from . import views

urlpatterns = [
    path('pricing/', views.subscription_price_view, name='pricing'),
    path('pricing/<str:interval>/', views.subscription_price_view, name='pricing-interval'),
    path('billing/', views.user_subscription_view, name='user_subscription'),
    path('billing/cancel', views.user_subscription_cancel_view, name='user_subscription_cancel'),
    ]