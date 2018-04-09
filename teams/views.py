from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from .models import TeamClassic, TeamTeamRebPct



def home_page_blk(request):
    context = {
    "title": "Home Page",
    "content": "This is home page",
    }
    return render(request, 'teams/blk_home.html', context)


def team_classic_shooting(request):
	#queryset = TeamClassic.objects.all()
	team_classic_shooting = TeamClassic.objects.values(
		'team', 'gp', 
        'two_fgm', 'two_fgms', 'two_prtg', 
		'three_fgm', 'three_fgms', 'three_prtg',
		'ftm', 'ftms', 'ft_prtg'
        )
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

        allz = TeamClassic.objects.values('team', 'gp', 'two_fgm')
        
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

        print('ft_prtg:', ft_prtg)


        #test
        two_fgm_mean = round(sum(two_fgm)/len(two_fgm),2)
        print(two_fgm_mean)

        lol = [two_fgm, two_fgms, two_prtg, three_fgm, three_fgms, three_prtg, ftm, ftms, ft_prtg]
        print('lol:', lol)

        lol2 = ['2FG Made','2FG Missed','2FG%','3FG Made','3FG Missed','3FG%','FT Made','FT Missed','FT%']
        reverse_gradient_flag = [0,1,0,0,1,0,0,1,0]


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
            'lol': lol,
            'lol2': lol2,
            'all': allz,
            'reverse_gradient_flag': reverse_gradient_flag,
            # 'labels': labels,
            # 'default': default_items,
            }
        return Response(data2)




### team_classing non shooting // do tabeli
def team_classic_nonshooting(request):
    team_classic_nonshooting = TeamClassic.objects.values(
        'team', 'gp',
        'off_reb', 'def_reb', 'tot_reb',
        'ast', 'stl', 'blk',
        'to', 'fls', 'mi','pts'
        )
    context = {
        'team_classic_nonshooting': team_classic_nonshooting
    }
    return render(request, "teams/team_classic_nonshooting.html", context)

## do wykresow
class team_classic_nonshooting_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        teams = TeamClassic.objects.values_list('team', flat=True)

        off_reb = TeamClassic.objects.values_list('off_reb', flat=True)
        def_reb = TeamClassic.objects.values_list('def_reb', flat=True)
        tot_reb = TeamClassic.objects.values_list('tot_reb', flat=True)

        ast = TeamClassic.objects.values_list('ast', flat=True)
        stl = TeamClassic.objects.values_list('stl', flat=True)
        blk = TeamClassic.objects.values_list('blk', flat=True)

        to = TeamClassic.objects.values_list('to', flat=True)
        fls = TeamClassic.objects.values_list('fls', flat=True)
        mi = TeamClassic.objects.values_list('mi', flat=True)

        pts = TeamClassic.objects.values_list('pts', flat=True)


        lol = [off_reb, def_reb, tot_reb, ast, stl, blk, to, fls, pts]
        lol2 = ['Off Reb','Def Reb','Tot Reb',
                'Ast','Stl','Blk',
                'Tov','Fouls','Points']
        reverse_gradient_flag = [0,0,0, 0,0,0, 1,0,0]


        data2 = {
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            }
        return Response(data2)









### team_team_reb_prtg // do tabeli
def team_team_reb_prtg(request):
    team_team_reb_prtg = TeamTeamRebPct.objects.values(
        'team', 'gp',
        'ors_m', 'ors_a', 'ors_prtg',
        'orb_m', 'orb_a', 'orb_prtg',
        'orf_m', 'orf_a', 'orf_prtg'
        )
    context = {
        'team_team_reb_prtg': team_team_reb_prtg
    }
    return render(request, "teams/team_team_reb_prtg.html", context)

## do wykresow
class team_team_reb_prtg_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        teams = TeamTeamRebPct.objects.values_list('team', flat=True)

        ors_m = TeamTeamRebPct.objects.values_list('ors_m', flat=True)
        ors_a = TeamTeamRebPct.objects.values_list('ors_a', flat=True)
        ors_prtg = TeamTeamRebPct.objects.values_list('ors_prtg', flat=True)

        orb_m = TeamTeamRebPct.objects.values_list('orb_m', flat=True)
        orb_a = TeamTeamRebPct.objects.values_list('orb_a', flat=True)
        orb_prtg = TeamTeamRebPct.objects.values_list('orb_prtg', flat=True)

        orf_m = TeamTeamRebPct.objects.values_list('orf_m', flat=True)
        orf_a = TeamTeamRebPct.objects.values_list('orf_a', flat=True)
        orf_prtg = TeamTeamRebPct.objects.values_list('orf_prtg', flat=True)


        lol = [ors_m, ors_a, ors_prtg, orb_m, orb_a, orb_prtg, orf_m, orf_a, orf_prtg,]
        lol2 = ['OR Made of Shots','OR Available of Shots','OR% Shots',
                'OR Made of Blocks','OR Available of Blocks','OR% Blocks',
                'OR Made of FT','OR Available of FT','OR%_FT']
        reverse_gradient_flag = [0,0,0, 0,0,0, 0,0,0]


        data2 = {
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            }
        return Response(data2)



### team_team_reb_prtg // do tabeli
def team_team_dreb_prtg(request):
    team_team_dreb_prtg = TeamTeamRebPct.objects.values(
        'team', 'gp',
        'drs_m', 'drs_a', 'drs_prtg',
        'drb_m', 'drb_a', 'drb_prtg',
        'drf_m', 'drf_a', 'drf_prtg'
        )
    context = {
        'team_team_dreb_prtg': team_team_dreb_prtg
    }
    return render(request, "teams/team_team_dreb_prtg.html", context)

## do wykresow
class team_team_dreb_prtg_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        teams = TeamTeamRebPct.objects.values_list('team', flat=True)

        drs_m = TeamTeamRebPct.objects.values_list('drs_m', flat=True)
        drs_a = TeamTeamRebPct.objects.values_list('drs_a', flat=True)
        drs_prtg = TeamTeamRebPct.objects.values_list('drs_prtg', flat=True)

        drb_m = TeamTeamRebPct.objects.values_list('drb_m', flat=True)
        drb_a = TeamTeamRebPct.objects.values_list('drb_a', flat=True)
        drb_prtg = TeamTeamRebPct.objects.values_list('drb_prtg', flat=True)

        drf_m = TeamTeamRebPct.objects.values_list('drf_m', flat=True)
        drf_a = TeamTeamRebPct.objects.values_list('drf_a', flat=True)
        drf_prtg = TeamTeamRebPct.objects.values_list('drf_prtg', flat=True)


        lol = [drs_m, drs_a, drs_prtg, drb_m, drb_a, drb_prtg, drf_m, drf_a, drf_prtg,]
        lol2 = ['DR Made of Shots','DR Available of Shots','DR% Shots',
                'DR Made of Blocks','DR Available of Blocks','DR% Blocks',
                'DR Made of FT','DR Available of FT','DR%_FT']
        reverse_gradient_flag = [0,0,0, 0,0,0, 0,0,0]


        data2 = {
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
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
