from django.shortcuts import render
from .forms import UserForm, ProfileForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from .models import Profile


@login_required
@transaction.atomic
def update_profile(request):
	
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request,'worker/success.html')
            
        else:
            return HttpResponse('Please correct the errors.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    	return render(request, 'worker/worker.html', {
        	'user_form': user_form,
        	'profile_form': profile_form
    	})

def view_profile(request):

    return render(request,'worker/view.html')