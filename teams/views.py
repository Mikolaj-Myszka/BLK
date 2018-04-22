from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from .models import TeamClassic, TeamTeamRebPct, TeamTeamPct, TeamTeamShotDiv, TeamTeamShotAdv, TeamSummary



def home_page_blk(request):
    context = {
    "title": "Home Page",
    "content": "This is home page",
    }
    return render(request, 'teams/blk_home.html', context)


def team_classic_shooting(request):
    #canvas = "hello"
    #queryset = TeamClassic.objects.all()
    page_title = 'Shooting Statistics'
    page_subtitle = 'Team / Classic'
    navbar_type = 0
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = TeamClassic.objects.values('team','gp','two_fgm','two_fgms','two_prtg','three_fgm','three_fgms','three_prtg','ftm','ftms','ft_prtg')
    table_col_names = ['Team','Games','2FG Made','2FG Missed','2FG%','3FG Made','3FG Missed','3FG%','FT Made','FT Missed','FT%']
    endpoint = '/blk/team-classic-shooting-api/'
    print(endpoint)
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "teams/team_universal.html", context)


#User = get_user_model()
class team_classic_shooting_API(APIView):
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
    page_title = 'Non-Shooting Statistics'
    page_subtitle = 'Team / Classic'
    navbar_type = 0 # 0 classic
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = TeamClassic.objects.values('team', 'gp','off_reb', 'def_reb', 'tot_reb','ast', 'stl', 'blk','to', 'fls', 'mi','pts')
    table_col_names = ['Team','Games','Off Reb','Def Reb','Tot Reb','Ast','Stl','Blk','Tov','Fls','Min','Pts']
    endpoint = '/blk/team-classic-nonshooting-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "teams/team_universal.html", context)

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
        lol2 = ['Off Reb','Def Reb','Tot Reb','Ast','Stl','Blk','Tov','Fouls','Points']
        reverse_gradient_flag = [0,0,0, 0,0,0, 1,0,0]


        data2 = {
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            }
        return Response(data2)









### team_team_oreb_prtg // do tabeli
def team_team_oreb_prtg(request):
    page_title = 'Offensive Rebounds Statistics'
    page_subtitle = 'Team / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = TeamTeamRebPct.objects.values('team', 'gp','ors_m', 'ors_a', 'ors_prtg','orb_m', 'orb_a', 'orb_prtg','orf_m', 'orf_a', 'orf_prtg')
    table_col_names = ['Team','Games',
                'Made (Shots)','Available (Shots)','OR% (Shots)',
                'Made (Blocks)','Available (Blocks)','OR% (Blocks)',
                'Made (FT)','Available (FT)','OR% (FT)']
    endpoint = '/blk/team-team-oreb-prtg-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "teams/team_universal.html", context)



## do wykresow
class team_team_oreb_prtg_API(APIView):
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
        lol2 = ['Made (Shots)','Available (Shots)','OR% (Shots)',
                'Made (Blocks)','Available (Blocks)','OR% (Blocks)',
                'Made (FT)','Available (FT)','OR% (FT)']
                
        reverse_gradient_flag = [0,0,0, 0,0,0, 0,0,0]


        data2 = {
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            }
        return Response(data2)



### team_team_dreb_prtg // do tabeli
def team_team_dreb_prtg(request):
    page_title = 'Defensive Rebounds Statistics'
    page_subtitle = 'Team / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = TeamTeamRebPct.objects.values('team', 'gp','drs_m', 'drs_a', 'drs_prtg','drb_m', 'drb_a', 'drb_prtg','drf_m', 'drf_a', 'drf_prtg')
    table_col_names = ['Team','Games',
                'Made (Shots)','Available (Shots)','DR% (Shots)',
                'Made (Blocks)','Available (Blocks)','DR% (Blocks)',
                'Made (FT)','Available (FT)','DR% (FT)']
    endpoint = '/blk/team-team-dreb-prtg-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "teams/team_universal.html", context)

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
        lol2 = ['Made (Shots)','Available (Shots)','DR% (Shots)',
                'Made (Blocks)','Available (Blocks)','DR% (Blocks)',
                'Made (FT)','Available (FT)','DR% (FT)']
        reverse_gradient_flag = [0,0,0, 0,0,0, 0,0,0]


        data2 = {
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            }
        return Response(data2)




### team_team_prtg // do tabeli
def team_team_prtg(request):
    page_title = 'Various Statistics'
    page_subtitle = 'Team / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6]
    table_cell_values = TeamTeamPct.objects.values('team', 'gp','ast_prtg', 'stl_prtg', 'blk_prtg','tov_prtg', 'fls_prtg')
    table_col_names = ['Team','Games',
                'Ast%','Stl%','Blk%','Tov%','Fls%']
    endpoint = '/blk/team-team-prtg-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "teams/team_universal.html", context)

## do wykresow
class team_team_prtg_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        teams = TeamTeamPct.objects.values_list('team', flat=True)

        ast_prtg = TeamTeamPct.objects.values_list('ast_prtg', flat=True)
        stl_prtg = TeamTeamPct.objects.values_list('stl_prtg', flat=True)
        blk_prtg = TeamTeamPct.objects.values_list('blk_prtg', flat=True)
        
        tov_prtg = TeamTeamPct.objects.values_list('tov_prtg', flat=True)
        fls_prtg = TeamTeamPct.objects.values_list('fls_prtg', flat=True)


        lol = [ast_prtg, stl_prtg, blk_prtg, tov_prtg, fls_prtg]
        lol2 = ['Ast%','Stl%','Blk%','Tov%','Fls%']
        reverse_gradient_flag = [0,0,0, 1,1,0]


        data2 = {
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            }
        return Response(data2)





### team_team_shot_div // do tabeli
def team_team_shot_div_0(request):
    page_title = 'Shot Division / 0-7 ft'
    page_subtitle = 'Team / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = TeamTeamShotDiv.objects.values('team', 'gp','zero_fgm', 'zero_fga', 'zero_pts','zero_ast', 
        'zero_fg_prtg', 'zero_prtg_fga', 'zero_prtg_ast', 'zero_prtg_pts')
    table_col_names = ['Team','Games','FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
    endpoint = '/blk/team-team-shot-div-0-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "teams/team_universal.html", context)


## do wykresow
class team_team_shot_div_0_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        teams = TeamTeamShotDiv.objects.values_list('team', flat=True)

        zero_fgm = TeamTeamShotDiv.objects.values_list('zero_fgm', flat=True)
        zero_fga = TeamTeamShotDiv.objects.values_list('zero_fga', flat=True)
        zero_pts = TeamTeamShotDiv.objects.values_list('zero_pts', flat=True)
        zero_ast = TeamTeamShotDiv.objects.values_list('zero_ast', flat=True)
        zero_fg_prtg = TeamTeamShotDiv.objects.values_list('zero_fg_prtg', flat=True)
        zero_prtg_fga = TeamTeamShotDiv.objects.values_list('zero_prtg_fga', flat=True)
        zero_prtg_ast = TeamTeamShotDiv.objects.values_list('zero_prtg_ast', flat=True)
        zero_prtg_pts = TeamTeamShotDiv.objects.values_list('zero_prtg_pts', flat=True)
        


        lol = [zero_fgm, zero_fga, zero_pts, zero_ast, zero_fg_prtg, zero_prtg_fga, zero_prtg_ast, zero_prtg_pts]
        lol2 = ['FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
        reverse_gradient_flag = [0,0,0, 0,0,0, 0,0]


        data2 = {
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            }
        return Response(data2)





### team_team_shot_div // do tabeli
def team_team_shot_div_8(request):
    page_title = 'Shot Division / 8-15 ft'
    page_subtitle = 'Team / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = TeamTeamShotDiv.objects.values('team', 'gp','eight_fgm', 'eight_fga', 'eight_pts','eight_ast', 
        'eight_fg_prtg', 'eight_prtg_fga', 'eight_prtg_ast', 'eight_prtg_pts')
    table_col_names = ['Team','Games','FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
    endpoint = '/blk/team-team-shot-div-8-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "teams/team_universal.html", context)


## do wykresow
class team_team_shot_div_8_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        teams = TeamTeamShotDiv.objects.values_list('team', flat=True)

        eight_fgm = TeamTeamShotDiv.objects.values_list('eight_fgm', flat=True)
        eight_fga = TeamTeamShotDiv.objects.values_list('eight_fga', flat=True)
        eight_pts = TeamTeamShotDiv.objects.values_list('eight_pts', flat=True)
        eight_ast = TeamTeamShotDiv.objects.values_list('eight_ast', flat=True)
        eight_fg_prtg = TeamTeamShotDiv.objects.values_list('eight_fg_prtg', flat=True)
        eight_prtg_fga = TeamTeamShotDiv.objects.values_list('eight_prtg_fga', flat=True)
        eight_prtg_ast = TeamTeamShotDiv.objects.values_list('eight_prtg_ast', flat=True)
        eight_prtg_pts = TeamTeamShotDiv.objects.values_list('eight_prtg_pts', flat=True)
        


        lol = [eight_fgm, eight_fga, eight_pts, eight_ast, eight_fg_prtg, eight_prtg_fga, eight_prtg_ast, eight_prtg_pts]
        lol2 = ['FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
        reverse_gradient_flag = [0,0,0, 0,0,0, 0,0]


        data2 = {
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            }
        return Response(data2)






### team_team_shot_div // do tabeli
def team_team_shot_div_16(request):
    page_title = 'Shot Division / 16 ft - 3PT'
    page_subtitle = 'Team / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = TeamTeamShotDiv.objects.values('team', 'gp','sixteen_fgm', 'sixteen_fga', 'sixteen_pts','sixteen_ast', 
        'sixteen_fg_prtg', 'sixteen_prtg_fga', 'sixteen_prtg_ast', 'sixteen_prtg_pts')
    table_col_names = ['Team','Games','FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
    endpoint = '/blk/team-team-shot-div-16-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "teams/team_universal.html", context)


## do wykresow
class team_team_shot_div_16_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        teams = TeamTeamShotDiv.objects.values_list('team', flat=True)

        sixteen_fgm = TeamTeamShotDiv.objects.values_list('sixteen_fgm', flat=True)
        sixteen_fga = TeamTeamShotDiv.objects.values_list('sixteen_fga', flat=True)
        sixteen_pts = TeamTeamShotDiv.objects.values_list('sixteen_pts', flat=True)
        sixteen_ast = TeamTeamShotDiv.objects.values_list('sixteen_ast', flat=True)
        sixteen_fg_prtg = TeamTeamShotDiv.objects.values_list('sixteen_fg_prtg', flat=True)
        sixteen_prtg_fga = TeamTeamShotDiv.objects.values_list('sixteen_prtg_fga', flat=True)
        sixteen_prtg_ast = TeamTeamShotDiv.objects.values_list('sixteen_prtg_ast', flat=True)
        sixteen_prtg_pts = TeamTeamShotDiv.objects.values_list('sixteen_prtg_pts', flat=True)
        


        lol = [sixteen_fgm, sixteen_fga, sixteen_pts, sixteen_ast, sixteen_fg_prtg, sixteen_prtg_fga, sixteen_prtg_ast, sixteen_prtg_pts]
        lol2 = ['FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
        reverse_gradient_flag = [0,0,0, 0,0,0, 0,0]


        data2 = {
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            }
        return Response(data2)






### team_team_shot_div // do tabeli
def team_team_shot_div_3(request):
    page_title = 'Shot Division / 3PT'
    page_subtitle = 'Team / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = TeamTeamShotDiv.objects.values('team', 'gp','three_fgm', 'three_fga', 'three_pts','three_ast', 
        'three_fg_prtg', 'three_prtg_fga', 'three_prtg_ast', 'three_prtg_pts')
    table_col_names = ['Team','Games','FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
    endpoint = '/blk/team-team-shot-div-3-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "teams/team_universal.html", context)


## do wykresow
class team_team_shot_div_3_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        teams = TeamTeamShotDiv.objects.values_list('team', flat=True)

        three_fgm = TeamTeamShotDiv.objects.values_list('three_fgm', flat=True)
        three_fga = TeamTeamShotDiv.objects.values_list('three_fga', flat=True)
        three_pts = TeamTeamShotDiv.objects.values_list('three_pts', flat=True)
        three_ast = TeamTeamShotDiv.objects.values_list('three_ast', flat=True)
        three_fg_prtg = TeamTeamShotDiv.objects.values_list('three_fg_prtg', flat=True)
        three_prtg_fga = TeamTeamShotDiv.objects.values_list('three_prtg_fga', flat=True)
        three_prtg_ast = TeamTeamShotDiv.objects.values_list('three_prtg_ast', flat=True)
        three_prtg_pts = TeamTeamShotDiv.objects.values_list('three_prtg_pts', flat=True)
        


        lol = [three_fgm, three_fga, three_pts, three_ast, three_fg_prtg, three_prtg_fga, three_prtg_ast, three_prtg_pts]
        lol2 = ['FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
        reverse_gradient_flag = [0,0,0, 0,0,0, 0,0]


        data2 = {
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            }
        return Response(data2)






### team_team_shot_div // do tabeli
def team_team_shot_adv(request):
    page_title = 'Shooting'
    page_subtitle = 'Team / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6]
    table_cell_values = TeamTeamShotAdv.objects.values('team','gp','efg_prtg','ts_prtg','usg_prtg','pps','avg_dist')
    table_col_names = ['Team','Games','eFG%','TS%','USG%','PP100S','AVG FT DIST']
    endpoint = '/blk/team-team-shot-adv-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "teams/team_universal.html", context)


## do wykresow
class team_team_shot_adv_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        teams = TeamTeamShotAdv.objects.values_list('team', flat=True)

        efg_prtg = TeamTeamShotAdv.objects.values_list('efg_prtg', flat=True)
        ts_prtg = TeamTeamShotAdv.objects.values_list('ts_prtg', flat=True)
        usg_prtg = TeamTeamShotAdv.objects.values_list('usg_prtg', flat=True)
        pps = TeamTeamShotAdv.objects.values_list('pps', flat=True)
        avg_dist = TeamTeamShotAdv.objects.values_list('avg_dist', flat=True)
        


        lol = [efg_prtg,ts_prtg,usg_prtg,pps,avg_dist]
        lol2 = ['eFG%','TS%','USG%','PP100S','AVG FT DIST']
        reverse_gradient_flag = [0,0,0, 0,0]


        data2 = {
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            }
        return Response(data2)





### team_summary // do tabeli
def team_summary(request):
    page_title = 'Summary'
    page_subtitle = 'Team / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = TeamSummary.objects.order_by('team').values('team','gp','wins','at_home','win_prtg','team_pts','team_poss',
        'off_rtg','oppo_pts','oppo_poss','def_rtg','net_rtg')
    table_col_names = ['Team','Games','Wins','@Home','Win%','Team Pts','Team Poss','OffRtg','Oppo Pts','Oppo Poss','DefRtg','NetRtg']
    endpoint = '/blk/team-summary-api/'
    # print(table_cell_values)
    # print(type(table_cell_values))
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "teams/team_universal.html", context)


## do wykresow
class team_summary_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        #TeamSummary = TeamSummary.objects.order_by('team')
        teams = TeamSummary.objects.order_by('team').values_list('team', flat=True)

        team_pts = TeamSummary.objects.order_by('team').values_list('team_pts', flat=True)
        team_poss = TeamSummary.objects.order_by('team').values_list('team_poss', flat=True)
        off_rtg = TeamSummary.objects.order_by('team').values_list('off_rtg', flat=True)

        oppo_pts = TeamSummary.objects.order_by('team').values_list('oppo_pts', flat=True)
        oppo_poss = TeamSummary.objects.order_by('team').values_list('oppo_poss', flat=True)
        def_rtg = TeamSummary.objects.order_by('team').values_list('def_rtg', flat=True)

        wins = TeamSummary.objects.order_by('team').values_list('wins', flat=True)
        win_prtg = TeamSummary.objects.order_by('team').values_list('win_prtg', flat=True)
        net_rtg = TeamSummary.objects.order_by('team').values_list('net_rtg', flat=True)
        

        lol = [team_pts,team_poss,off_rtg,oppo_pts,oppo_poss,def_rtg,wins,win_prtg,net_rtg]
        lol2 = ['Team Pts','Team Poss','OffRtg','Oppo Pts','Oppo Poss','DefRtg','Wins','Win%','NetRtg']
        reverse_gradient_flag = [0,0,0, 1,0,1, 0,0,0]


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
