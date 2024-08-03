from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
@login_required
def profile_list_view(request):
    context = {
        'object_list': User.objects.filter(is_active=True)
    }
    return render(request, 'profiles/list.html', context)

@login_required
def profile_detail_view(request, username=None,*args,**kwargs):
    user = request.user
    print(
        user.has_perm('subscriptions.basic'),
        user.has_perm('subscriptions.pro'),
        user.has_perm('subscriptions.advanced'),
        )
    # user_groups = user.groups.all()
    # print('user groups: ', user_groups)
    profile_user_obj = get_object_or_404(User, username=username) # profile_user_obj = User.objects.get(username=username)
    is_me = profile_user_obj==user
    context = {
        'object': profile_user_obj,
        'instance': profile_user_obj,
        'owner': is_me,
    }
    return render(request, 'profiles/detail.html', context)