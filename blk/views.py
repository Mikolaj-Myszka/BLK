from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
	context = {
	"title": "Home Page",
	"content": "This is home page",
	}
	# print(context)
	# if request.user.is_authenticated():
	# 	context["premium_content"] = "YEAHHHH"
	# 	print(context)
	# 	print(request.user.is_authenticated())
	# 	print(request.user.is_authenticated)
	# 	print(request.user)
	# 	print(request)
	return render(request, 'home_page.html', context)