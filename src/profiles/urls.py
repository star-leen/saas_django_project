from . import views
from django.urls import path, include



urlpatterns = [
    path('', views.profile_list_view, name='profile_list'),
    path('<str:username>/', views.profile_detail_view, name='profile'),    
]
