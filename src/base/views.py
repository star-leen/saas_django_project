from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_view(request):
    context = {}
    return render(request, 'home.html', context)

@login_required
def user_only_view(request):
    return render(request, 'protected/user-only.html', {})