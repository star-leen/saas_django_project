from django.urls import path
from . import views

urlpatterns = [
    path('sub-price/<int:price_id>/', views.product_price_redirect_view, name='sub-price-checkout'),
    path('start/', views.checkout_redirect_view, name='stripe-checkout-start'),
    path('success/', views.checkout_finalize_view, name='stripe-checkout-end'),
    ]
