from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
	print(request.user.is_authenticated())
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username = username, password = password)
		login(request,user)
		print(request.user.is_authenticated())
		return render(request,'worker/viewedit.html')
		
	else:
		return render(request,'login/form.html',{"form":form,})

def register_view(request):
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit = False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		myuser = authenticate(username = user.username, password = password)
		login(request,myuser)
		return render(request,'worker/viewedit.html')



	else:
		context = {
		'form' : form
		}
		return render(request,'login/register.html',context)

def logout_view(request):
	form = UserLoginForm(request.POST or None)
	logout(request)
	#return render(request,'login/form.html',{'form' : form})
	return render(request,'login/logout.html')