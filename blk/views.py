from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm


def home_page(request):
	# context = {
	# "title": "Home Page",
	# "content": "This is home page",
	# }
	# print(context)
	# if request.user.is_authenticated():
	# 	context["premium_content"] = "YEAHHHH"
	# 	print(context)
	# 	print(request.user.is_authenticated())
	# 	print(request.user.is_authenticated)
	# 	print(request.user)
	# 	print(request)

	#Login
	form = LoginForm(request.POST or None)
	context = {
		"form": form
	}
	
	print(context)
	print('1. Is user authenticated:', request.user.is_authenticated())
	
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')

		user = authenticate(request, username=username, password=password)
		print('user:', user)
		print('2. Is user authenticated:', request.user.is_authenticated())
		
		if user is not None:
			login(request, user)
			print('3. Is user authenticated (after login):', request.user.is_authenticated())
			# Redirect to a success page.
			return redirect('blk:blk_home')
		else:
		# Return an 'invalid login' error message.
			print('Error')

	return render(request, 'home_page.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')