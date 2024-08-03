"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    # path('login/', auth_views.login_view, name='login'),
    # path('register/', auth_views.register_view, name='register'),
    path('protected/user-only', views.user_only_view, name='user-only'),
    path('profiles/', include('profiles.urls')),
    # Django AllAuth Url:
    path('accounts/', include('allauth.urls')),
    path('subscriptions/', include('subscriptions.urls')),
    path('checkout/', include('checkout.urls')),
    path('admin/', admin.site.urls),
]
