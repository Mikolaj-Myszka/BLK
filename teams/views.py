from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from .models import TeamClassic



def home_page_blk(request):
    context = {
    "title": "Home Page",
    "content": "This is home page",
    }
    return render(request, 'teams/blk_home.html', context)


def team_classic_shooting(request):
	#queryset = TeamClassic.objects.all()
	team_classic_shooting = TeamClassic.objects.values(
		'team', 'gp', 'two_fgm', 'two_fgms', 'two_prtg', 
		'three_fgm', 'three_fgms', 'three_prtg',
		'ftm', 'ftms', 'ft_prtg')
	context = {
		#'object_list': queryset,
		'team_classic_shooting': team_classic_shooting
	}
	return render(request, "teams/team_classic_shooting.html", context)



#User = get_user_model()
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        #qs_count = User.objects.all().count()
        #labels = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
        #default_items = [qs_count, 3, 5, 7, 8, 2]

        
        """q2 = TeamClassic.objects.values('team', 'gp')
        print(q2)"""
        
        teams = TeamClassic.objects.values_list('team', flat=True)

        two_fgm = TeamClassic.objects.values_list('two_fgm', flat=True)
        two_fgms = TeamClassic.objects.values_list('two_fgms', flat=True)
        two_prtg = TeamClassic.objects.values_list('two_prtg', flat=True)

        three_fgm = TeamClassic.objects.values_list('three_fgm', flat=True)
        three_fgms = TeamClassic.objects.values_list('three_fgms', flat=True)
        three_prtg = TeamClassic.objects.values_list('three_prtg', flat=True)

        ftm = TeamClassic.objects.values_list('ftm', flat=True)
        ftms = TeamClassic.objects.values_list('ftms', flat=True)
        ft_prtg = TeamClassic.objects.values_list('ft_prtg', flat=True)


        data2 = {
            'teams': teams,
            'two_fgm': two_fgm,
            'two_fgms': two_fgms,
            'two_prtg': two_prtg,
            'three_fgm': three_fgm,
            'three_fgms': three_fgms,
            'three_prtg': three_prtg,
            'ftm': ftm,
            'ftms': ftms,
            'ft_prtg': ft_prtg,
            # 'labels': labels,
            # 'default': default_items,
            }
        return Response(data2)



# def graph_view(request):
# 	queryset = TeamClassic.objects.all()
# 	print('queryset: ', queryset)
# 	#print('number: ', number)
# 	context = {
# 		'object_list': queryset,
# 		'number': 4,
# 		'customers': 7,
# 	}
# 	print(context)
# 	return render(request, "teams/graph.html", context)


# def get_data(request, *args, **kwargs):
# 	data = {
# 		'sales': 100,
# 		'customers': 70,
# 	}
# 	return JsonResponse(data) # http response still




