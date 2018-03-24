from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from .models import TeamClassic

def team_page(request):
	return HttpResponse("<h1>Hello Mamma and Kitty!</h1>")


def team_list_view(request):
	queryset = TeamClassic.objects.all()
	q2 = TeamClassic.objects.values('team', 'gp', 'two_fgm', 'two_fgms', 'two_prtg')
	context = {
		'object_list': queryset,
		'q2': q2
	}
	return render(request, "teams/list.html", context)



def graph_view(request):
	queryset = TeamClassic.objects.all()
	print('queryset: ', queryset)
	#print('number: ', number)
	context = {
		'object_list': queryset,
		'number': 4,
		'customers': 7,
	}
	print(context)
	return render(request, "teams/graph.html", context)


def get_data(request, *args, **kwargs):
	data = {
		'sales': 100,
		'customers': 70,
	}
	return JsonResponse(data) # http response still


User = get_user_model()
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
    	qs_count = User.objects.all().count()
    	labels = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
    	default_items = [qs_count, 3, 5, 7, 8, 2]


    	q2 = TeamClassic.objects.values('team', 'gp')
    	print(q2)
    	
    	q = TeamClassic.objects.values_list('team', flat=True)
    	q1 = TeamClassic.objects.values_list('pts', flat=True)
    	q3 = TeamClassic.objects.values_list('ast', flat=True)
    	print(q)
    	print(q1)





    	data = {
    		'labels': labels,
    		'default': default_items,
    		'q': q,
    		'q1':q1,
    		'q2': q2,
    		'q3': q3,
    		}
    	return Response(data)
