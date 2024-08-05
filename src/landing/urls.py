from . import views
from django.urls import path

urlpatterns = [
    path('', views.landing_dashboard_page_view, name='home'),
]