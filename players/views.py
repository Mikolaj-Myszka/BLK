from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from .models import PlayerClassic, PlayerTeamRebPct, PlayerTeamPct, PlayerTeamShotDiv, PlayerTeamShotAdv #, TeamSummary


def player_classic_shooting(request):
    #canvas = "hello"
    #queryset = PlayerClassic.objects.all()
    page_title = 'Shooting Statistics'
    page_subtitle = 'Player / Classic'
    navbar_type = 0
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = PlayerClassic.objects.values('player','team','gp','gs','two_fgm','two_fgms','two_prtg','three_fgm','three_fgms','three_prtg','ftm','ftms','ft_prtg')
    table_col_names = ['Player','Tm','G','GS','2M','2Ms','2FG%','3M','3Ms','3FG%','FTM','FTMs','FT%']
    endpoint = '/blk/player-classic-shooting-api/'
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
    return render(request, "players/player_universal.html", context)



#User = get_user_model()
class player_classic_shooting_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        #qs_count = User.objects.all().count()
        #labels = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
        #default_items = [qs_count, 3, 5, 7, 8, 2]

        
        #q2 = TeamClassic.objects.values('team', 'gp')
        #print(q2)

        players = PlayerClassic.objects.values_list('player', flat=True)
        teams = PlayerClassic.objects.values_list('team', flat=True)

        two_fgm = PlayerClassic.objects.values_list('two_fgm', flat=True)
        two_fgms = PlayerClassic.objects.values_list('two_fgms', flat=True)
        two_prtg = PlayerClassic.objects.values_list('two_prtg', flat=True)

        three_fgm = PlayerClassic.objects.values_list('three_fgm', flat=True)
        three_fgms = PlayerClassic.objects.values_list('three_fgms', flat=True)
        three_prtg = PlayerClassic.objects.values_list('three_prtg', flat=True)

        ftm = PlayerClassic.objects.values_list('ftm', flat=True)
        ftms = PlayerClassic.objects.values_list('ftms', flat=True)
        ft_prtg = PlayerClassic.objects.values_list('ft_prtg', flat=True)

        print('ft_prtg:', ft_prtg)


        #test
        two_fgm_mean = round(sum(two_fgm)/len(two_fgm),2)
        print(two_fgm_mean)

        lol = [two_fgm, two_fgms, two_prtg, three_fgm, three_fgms, three_prtg, ftm, ftms, ft_prtg]
        print('lol:', lol)

        lol2 = ['2FG Made','2FG Missed','2FG%','3FG Made','3FG Missed','3FG%','FT Made','FT Missed','FT%']
        reverse_gradient_flag = [0,1,0,0,1,0,0,1,0]

        averages = [round(my_mean(two_fgm),2), round(my_mean(two_fgms),2), round(my_mean(two_prtg),2),
                    round(my_mean(three_fgm),2), round(my_mean(three_fgms),2), round(my_mean(three_prtg),2),
                    round(my_mean(ftm),2), round(my_mean(ftms),2), round(my_mean(ft_prtg),2)]


        data2 = {
            'players': players,
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            'averages': averages,
            # 'labels': labels,
            # 'default': default_items,
            }
        return Response(data2)




### team_classing non shooting // do tabeli
def player_classic_nonshooting(request):
    page_title = 'Non-Shooting Statistics'
    page_subtitle = 'Player / Classic'
    navbar_type = 0 # 0 classic
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = PlayerClassic.objects.values('player','team','gp','gs','off_reb', 'def_reb', 'tot_reb','ast', 'stl', 'blk','to', 'fls', 'mi','pts')
    table_col_names = ['Player','Tm','G','GS','OR','DR','TR','Ast','Stl','Blk','Tov','Fls','Min','Pts']
    endpoint = '/blk/player-classic-nonshooting-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "players/player_universal.html", context)

## do wykresow
class player_classic_nonshooting_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        players = PlayerClassic.objects.values_list('player', flat=True)
        teams = PlayerClassic.objects.values_list('team', flat=True)

        off_reb = PlayerClassic.objects.values_list('off_reb', flat=True)
        def_reb = PlayerClassic.objects.values_list('def_reb', flat=True)
        tot_reb = PlayerClassic.objects.values_list('tot_reb', flat=True)

        ast = PlayerClassic.objects.values_list('ast', flat=True)
        stl = PlayerClassic.objects.values_list('stl', flat=True)
        blk = PlayerClassic.objects.values_list('blk', flat=True)

        to = PlayerClassic.objects.values_list('to', flat=True)
        fls = PlayerClassic.objects.values_list('fls', flat=True)
        mi = PlayerClassic.objects.values_list('mi', flat=True)

        pts = PlayerClassic.objects.values_list('pts', flat=True)


        lol = [off_reb, def_reb, tot_reb, ast, stl, blk, to, fls, pts]
        lol2 = ['Off Reb','Def Reb','Tot Reb','Ast','Stl','Blk','Tov','Fouls','Points']
        reverse_gradient_flag = [0,0,0, 0,0,0, 1,0,0]

        averages = [round(my_mean(off_reb),2), round(my_mean(def_reb),2), round(my_mean(tot_reb),2),
                    round(my_mean(ast),2), round(my_mean(stl),2), round(my_mean(blk),2),
                    round(my_mean(to),2), round(my_mean(fls),2), round(my_mean(pts),2)]


        data2 = {
            'players': players,
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            'averages': averages,
            }
        return Response(data2)









### player_team_oreb_prtg // do tabeli
def player_team_oreb_prtg(request):
    page_title = 'Offensive Rebounds Statistics'
    page_subtitle = 'Player / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = PlayerTeamRebPct.objects.values('player','team', 'gp','ors_m', 'ors_a', 'ors_prtg','orb_m', 'orb_a', 'orb_prtg','orf_m', 'orf_a', 'orf_prtg')
    table_col_names = ['Player','Tm','G',
                'M','A','OR%(Shots)',
                'M','A','OR%(Blocks)',
                'M','A','OR%(FT)']
    endpoint = '/blk/player-team-oreb-prtg-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "players/player_universal.html", context)



## do wykresow
class player_team_oreb_prtg_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        players = PlayerTeamRebPct.objects.values_list('player', flat=True)
        teams = PlayerTeamRebPct.objects.values_list('team', flat=True)

        ors_m = PlayerTeamRebPct.objects.values_list('ors_m', flat=True)
        ors_a = PlayerTeamRebPct.objects.values_list('ors_a', flat=True)
        ors_prtg = PlayerTeamRebPct.objects.values_list('ors_prtg', flat=True)

        orb_m = PlayerTeamRebPct.objects.values_list('orb_m', flat=True)
        orb_a = PlayerTeamRebPct.objects.values_list('orb_a', flat=True)
        orb_prtg = PlayerTeamRebPct.objects.values_list('orb_prtg', flat=True)

        orf_m = PlayerTeamRebPct.objects.values_list('orf_m', flat=True)
        orf_a = PlayerTeamRebPct.objects.values_list('orf_a', flat=True)
        orf_prtg = PlayerTeamRebPct.objects.values_list('orf_prtg', flat=True)


        lol = [ors_m, ors_a, ors_prtg, orb_m, orb_a, orb_prtg, orf_m, orf_a, orf_prtg,]
        lol2 = ['Made (Shots)','Available (Shots)','OR% (Shots)',
                'Made (Blocks)','Available (Blocks)','OR% (Blocks)',
                'Made (FT)','Available (FT)','OR% (FT)']
                
        reverse_gradient_flag = [0,0,0, 0,0,0, 0,0,0]

        averages = [round(my_mean(ors_m),2), round(my_mean(ors_a),2), round(my_mean(ors_prtg),2),
                    round(my_mean(orb_m),2), round(my_mean(orb_a),2), round(my_mean(orb_prtg),2),
                    round(my_mean(orf_m),2), round(my_mean(orf_a),2), round(my_mean(orf_prtg),2)]


        data2 = {
            'players': players,
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            'averages': averages,
            }
        return Response(data2)



### player_team_dreb_prtg // do tabeli
def player_team_dreb_prtg(request):
    page_title = 'Defensive Rebounds Statistics'
    page_subtitle = 'Player / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = PlayerTeamRebPct.objects.values('player','team', 'gp','drs_m', 'drs_a', 'drs_prtg','drb_m', 'drb_a', 'drb_prtg','drf_m', 'drf_a', 'drf_prtg')
    table_col_names = ['Player','Tm','G',
                'M','A','DR%(Shots)',
                'M','A','DR%(Blocks)',
                'M','A','DR%(FT)']
    endpoint = '/blk/player-team-dreb-prtg-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "players/player_universal.html", context)

## do wykresow
class player_team_dreb_prtg_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        players = PlayerTeamRebPct.objects.values_list('player', flat=True)
        teams = PlayerTeamRebPct.objects.values_list('team', flat=True)

        drs_m = PlayerTeamRebPct.objects.values_list('drs_m', flat=True)
        drs_a = PlayerTeamRebPct.objects.values_list('drs_a', flat=True)
        drs_prtg = PlayerTeamRebPct.objects.values_list('drs_prtg', flat=True)

        drb_m = PlayerTeamRebPct.objects.values_list('drb_m', flat=True)
        drb_a = PlayerTeamRebPct.objects.values_list('drb_a', flat=True)
        drb_prtg = PlayerTeamRebPct.objects.values_list('drb_prtg', flat=True)

        drf_m = PlayerTeamRebPct.objects.values_list('drf_m', flat=True)
        drf_a = PlayerTeamRebPct.objects.values_list('drf_a', flat=True)
        drf_prtg = PlayerTeamRebPct.objects.values_list('drf_prtg', flat=True)


        lol = [drs_m, drs_a, drs_prtg, drb_m, drb_a, drb_prtg, drf_m, drf_a, drf_prtg,]
        lol2 = ['Made (Shots)','Available (Shots)','DR% (Shots)',
                'Made (Blocks)','Available (Blocks)','DR% (Blocks)',
                'Made (FT)','Available (FT)','DR% (FT)']
        reverse_gradient_flag = [0,0,0, 0,0,0, 0,0,0]

        averages = [round(my_mean(drs_m),2), round(my_mean(drs_a),2), round(my_mean(drs_prtg),2),
                    round(my_mean(drb_m),2), round(my_mean(drb_a),2), round(my_mean(drb_prtg),2),
                    round(my_mean(drf_m),2), round(my_mean(drf_a),2), round(my_mean(drf_prtg),2)]


        data2 = {
            'players': players,
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            'averages': averages,
            }
        return Response(data2)




### player_team_prtg // do tabeli
def player_team_prtg(request):
    page_title = 'Various Statistics'
    page_subtitle = 'Player / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6]
    table_cell_values = PlayerTeamPct.objects.values('player','team', 'gp','ast_prtg', 'stl_prtg', 'blk_prtg','tov_prtg', 'fls_prtg')
    table_col_names = ['Player','Tm','G',
                'Ast%','Stl%','Blk%','Tov%','Fls%']
    endpoint = '/blk/player-team-prtg-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "players/player_universal.html", context)

## do wykresow
class player_team_prtg_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        players = PlayerTeamPct.objects.values_list('player', flat=True)
        teams = PlayerTeamPct.objects.values_list('team', flat=True)

        ast_prtg = PlayerTeamPct.objects.values_list('ast_prtg', flat=True)
        stl_prtg = PlayerTeamPct.objects.values_list('stl_prtg', flat=True)
        blk_prtg = PlayerTeamPct.objects.values_list('blk_prtg', flat=True)
        
        tov_prtg = PlayerTeamPct.objects.values_list('tov_prtg', flat=True)
        fls_prtg = PlayerTeamPct.objects.values_list('fls_prtg', flat=True)


        lol = [ast_prtg, stl_prtg, blk_prtg, tov_prtg, fls_prtg]
        lol2 = ['Ast%','Stl%','Blk%','Tov%','Fls%']
        reverse_gradient_flag = [0,0,0, 1,1,0]

        averages = [round(my_mean(ast_prtg),2), round(my_mean(stl_prtg),2), round(my_mean(blk_prtg),2),
                    round(my_mean(tov_prtg),2), round(my_mean(fls_prtg),2)]

        data2 = {
            'players': players,
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            'averages': averages
            }
        return Response(data2)





### player_team_shot_div // do tabeli
def player_team_shot_div_0(request):
    page_title = 'Shot Division / 0-7 ft'
    page_subtitle = 'Player / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = PlayerTeamShotDiv.objects.values('player','team', 'gp','zero_fgm', 'zero_fga', 'zero_pts','zero_ast', 
        'zero_fg_prtg', 'zero_prtg_fga', 'zero_prtg_ast', 'zero_prtg_pts')
    table_col_names = ['Player','Tm','G','FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
    endpoint = '/blk/player-team-shot-div-0-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "players/player_universal.html", context)


## do wykresow
class player_team_shot_div_0_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        players = PlayerTeamShotDiv.objects.values_list('player', flat=True)
        teams = PlayerTeamShotDiv.objects.values_list('team', flat=True)

        zero_fgm = PlayerTeamShotDiv.objects.values_list('zero_fgm', flat=True)
        zero_fga = PlayerTeamShotDiv.objects.values_list('zero_fga', flat=True)
        zero_pts = PlayerTeamShotDiv.objects.values_list('zero_pts', flat=True)
        zero_ast = PlayerTeamShotDiv.objects.values_list('zero_ast', flat=True)
        zero_fg_prtg = PlayerTeamShotDiv.objects.values_list('zero_fg_prtg', flat=True)
        zero_prtg_fga = PlayerTeamShotDiv.objects.values_list('zero_prtg_fga', flat=True)
        zero_prtg_ast = PlayerTeamShotDiv.objects.values_list('zero_prtg_ast', flat=True)
        zero_prtg_pts = PlayerTeamShotDiv.objects.values_list('zero_prtg_pts', flat=True)
        


        lol = [zero_fgm, zero_fga, zero_pts, zero_ast, zero_fg_prtg, zero_prtg_fga, zero_prtg_ast, zero_prtg_pts]
        lol2 = ['FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
        reverse_gradient_flag = [0,0,0, 0,0,0, 0,0]

        averages = [round(my_mean(zero_fgm),2), round(my_mean(zero_fga),2), round(my_mean(zero_pts),2),
                    round(my_mean(zero_ast),2), round(my_mean(zero_fg_prtg),2), round(my_mean(zero_prtg_fga),2),
                    round(my_mean(zero_prtg_ast),2), round(my_mean(zero_prtg_pts),2)]


        data2 = {
            'players': players,
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            'averages': averages,
            }
        return Response(data2)





### player_team_shot_div // do tabeli
def player_team_shot_div_8(request):
    page_title = 'Shot Division / 8-15 ft'
    page_subtitle = 'Player / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = PlayerTeamShotDiv.objects.values('player','team', 'gp','eight_fgm', 'eight_fga', 'eight_pts','eight_ast', 
        'eight_fg_prtg', 'eight_prtg_fga', 'eight_prtg_ast', 'eight_prtg_pts')
    table_col_names = ['Player','Tm','G','FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
    endpoint = '/blk/player-team-shot-div-8-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "players/player_universal.html", context)


## do wykresow
class player_team_shot_div_8_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        players = PlayerTeamShotDiv.objects.values_list('player', flat=True)
        teams = PlayerTeamShotDiv.objects.values_list('team', flat=True)

        eight_fgm = PlayerTeamShotDiv.objects.values_list('eight_fgm', flat=True)
        eight_fga = PlayerTeamShotDiv.objects.values_list('eight_fga', flat=True)
        eight_pts = PlayerTeamShotDiv.objects.values_list('eight_pts', flat=True)
        eight_ast = PlayerTeamShotDiv.objects.values_list('eight_ast', flat=True)
        eight_fg_prtg = PlayerTeamShotDiv.objects.values_list('eight_fg_prtg', flat=True)
        eight_prtg_fga = PlayerTeamShotDiv.objects.values_list('eight_prtg_fga', flat=True)
        eight_prtg_ast = PlayerTeamShotDiv.objects.values_list('eight_prtg_ast', flat=True)
        eight_prtg_pts = PlayerTeamShotDiv.objects.values_list('eight_prtg_pts', flat=True)
        


        lol = [eight_fgm, eight_fga, eight_pts, eight_ast, eight_fg_prtg, eight_prtg_fga, eight_prtg_ast, eight_prtg_pts]
        lol2 = ['FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
        reverse_gradient_flag = [0,0,0, 0,0,0, 0,0]

        averages = [round(my_mean(eight_fgm),2), round(my_mean(eight_fga),2), round(my_mean(eight_pts),2),
                    round(my_mean(eight_ast),2), round(my_mean(eight_fg_prtg),2), round(my_mean(eight_prtg_fga),2),
                    round(my_mean(eight_prtg_ast),2), round(my_mean(eight_prtg_pts),2)]


        data2 = {
            'players': players,
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            'averages': averages,
            }
        return Response(data2)






### player_team_shot_div // do tabeli
def player_team_shot_div_16(request):
    page_title = 'Shot Division / 16 ft - 3PT'
    page_subtitle = 'Player / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = PlayerTeamShotDiv.objects.values('player','team', 'gp','sixteen_fgm', 'sixteen_fga', 'sixteen_pts','sixteen_ast', 
        'sixteen_fg_prtg', 'sixteen_prtg_fga', 'sixteen_prtg_ast', 'sixteen_prtg_pts')
    table_col_names = ['Player','Tm','G','FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
    endpoint = '/blk/player-team-shot-div-16-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "players/player_universal.html", context)


## do wykresow
class player_team_shot_div_16_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        players = PlayerTeamShotDiv.objects.values_list('player', flat=True)
        teams = PlayerTeamShotDiv.objects.values_list('team', flat=True)

        sixteen_fgm = PlayerTeamShotDiv.objects.values_list('sixteen_fgm', flat=True)
        sixteen_fga = PlayerTeamShotDiv.objects.values_list('sixteen_fga', flat=True)
        sixteen_pts = PlayerTeamShotDiv.objects.values_list('sixteen_pts', flat=True)
        sixteen_ast = PlayerTeamShotDiv.objects.values_list('sixteen_ast', flat=True)
        sixteen_fg_prtg = PlayerTeamShotDiv.objects.values_list('sixteen_fg_prtg', flat=True)
        sixteen_prtg_fga = PlayerTeamShotDiv.objects.values_list('sixteen_prtg_fga', flat=True)
        sixteen_prtg_ast = PlayerTeamShotDiv.objects.values_list('sixteen_prtg_ast', flat=True)
        sixteen_prtg_pts = PlayerTeamShotDiv.objects.values_list('sixteen_prtg_pts', flat=True)
        


        lol = [sixteen_fgm, sixteen_fga, sixteen_pts, sixteen_ast, sixteen_fg_prtg, sixteen_prtg_fga, sixteen_prtg_ast, sixteen_prtg_pts]
        lol2 = ['FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
        reverse_gradient_flag = [0,0,0, 0,0,0, 0,0]

        averages = [round(my_mean(sixteen_fgm),2), round(my_mean(sixteen_fga),2), round(my_mean(sixteen_pts),2),
                    round(my_mean(sixteen_ast),2), round(my_mean(sixteen_fg_prtg),2), round(my_mean(sixteen_prtg_fga),2),
                    round(my_mean(sixteen_prtg_ast),2), round(my_mean(sixteen_prtg_pts),2)]


        data2 = {
            'players': players,
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            'averages': averages,
            }
        return Response(data2)






### player_team_shot_div // do tabeli
def player_team_shot_div_3(request):
    page_title = 'Shot Division / 3PT'
    page_subtitle = 'Player / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6,7,8,9]
    table_cell_values = PlayerTeamShotDiv.objects.values('player','team', 'gp','three_fgm', 'three_fga', 'three_pts','three_ast', 
        'three_fg_prtg', 'three_prtg_fga', 'three_prtg_ast', 'three_prtg_pts')
    table_col_names = ['Player','Tm','G','FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
    endpoint = '/blk/player-team-shot-div-3-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "players/player_universal.html", context)


## do wykresow
class player_team_shot_div_3_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        players = PlayerTeamShotDiv.objects.values_list('player', flat=True)
        teams = PlayerTeamShotDiv.objects.values_list('team', flat=True)

        three_fgm = PlayerTeamShotDiv.objects.values_list('three_fgm', flat=True)
        three_fga = PlayerTeamShotDiv.objects.values_list('three_fga', flat=True)
        three_pts = PlayerTeamShotDiv.objects.values_list('three_pts', flat=True)
        three_ast = PlayerTeamShotDiv.objects.values_list('three_ast', flat=True)
        three_fg_prtg = PlayerTeamShotDiv.objects.values_list('three_fg_prtg', flat=True)
        three_prtg_fga = PlayerTeamShotDiv.objects.values_list('three_prtg_fga', flat=True)
        three_prtg_ast = PlayerTeamShotDiv.objects.values_list('three_prtg_ast', flat=True)
        three_prtg_pts = PlayerTeamShotDiv.objects.values_list('three_prtg_pts', flat=True)
        


        lol = [three_fgm, three_fga, three_pts, three_ast, three_fg_prtg, three_prtg_fga, three_prtg_ast, three_prtg_pts]
        lol2 = ['FGM','FGA','PTS','AST','FG%','%FGA','%AST','%PTS']
        reverse_gradient_flag = [0,0,0, 0,0,0, 0,0]

        averages = [round(my_mean(three_fgm),2), round(my_mean(three_fga),2), round(my_mean(three_pts),2),
                    round(my_mean(three_ast),2), round(my_mean(three_fg_prtg),2), round(my_mean(three_prtg_fga),2),
                    round(my_mean(three_prtg_ast),2), round(my_mean(three_prtg_pts),2)]


        data2 = {
            'players': players,
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            'averages': averages,
            }
        return Response(data2)






### player_team_shot_div // do tabeli
def player_team_shot_adv(request):
    page_title = 'Shooting'
    page_subtitle = 'Player / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6]
    table_cell_values = PlayerTeamShotAdv.objects.values('player','team','gp','efg_prtg','ts_prtg','usg_prtg','pps','avg_dist')
    table_col_names = ['Player','Tm','G','eFG%','TS%','USG%','PP100S','Avg Ft Dist']
    endpoint = '/blk/player-team-shot-adv-api/'
    context = {
        'page_title': page_title,
        'page_subtitle': page_subtitle,
        'navbar_type': navbar_type,
        'canvas': canvas,
        'table_cell_values': table_cell_values,
        'table_col_names': table_col_names,
        'endpoint2': endpoint
        }
    return render(request, "players/player_universal.html", context)


## do wykresow
class player_team_shot_adv_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        players = PlayerTeamShotAdv.objects.values_list('player', flat=True)
        teams = PlayerTeamShotAdv.objects.values_list('team', flat=True)

        efg_prtg = PlayerTeamShotAdv.objects.values_list('efg_prtg', flat=True)
        ts_prtg = PlayerTeamShotAdv.objects.values_list('ts_prtg', flat=True)
        usg_prtg = PlayerTeamShotAdv.objects.values_list('usg_prtg', flat=True)
        pps = PlayerTeamShotAdv.objects.values_list('pps', flat=True)
        avg_dist = PlayerTeamShotAdv.objects.values_list('avg_dist', flat=True)
        


        lol = [efg_prtg,ts_prtg,usg_prtg,pps,avg_dist]
        lol2 = ['eFG%','TS%','USG%','PP100S','Avg Ft Dist']
        reverse_gradient_flag = [0,0,0, 0,0]

        averages = [round(my_mean(efg_prtg),2), round(my_mean(ts_prtg),2), round(my_mean(usg_prtg),2),
                    round(my_mean(pps),2), round(my_mean(avg_dist),2)]


        data2 = {
            'players': players,
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            'averages': averages,
            }
        return Response(data2)




"""
### player_summary // do tabeli
def player_summary(request):
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
class player_summary_API(APIView):
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


        averages = [round(my_mean(team_pts),2), round(my_mean(team_poss),2), round(my_mean(off_rtg),2),
                    round(my_mean(oppo_pts),2), round(my_mean(oppo_poss),2), round(my_mean(def_rtg),2),
                    round(my_mean(wins),2), round(my_mean(win_prtg),2), round(my_mean(net_rtg),2)]


        data2 = {
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            'averages': averages,
            }
        return Response(data2)



### player_summary // do tabeli
def team_dashboard(request):
    page_title = 'Dashboard'
    page_subtitle = 'Team / Advanced'
    navbar_type = 1 # 0 classic / 1 Advanced
    canvas = [1,2,3,4,5,6,7,8,9]
    test = TeamSummary.objects.all()
    print('test:', test)
    table_cell_values = TeamSummary.objects.order_by('team').values('team','gp','wins','at_home','win_prtg','team_pts','team_poss',
        'off_rtg','oppo_pts','oppo_poss','def_rtg','net_rtg')
    table_col_names = ['Team','Games','Wins','@Home','Win%','Team Pts','Team Poss','OffRtg','Oppo Pts','Oppo Poss','DefRtg','NetRtg']
    endpoint = '/blk/team-dashboard-api/'
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
    return render(request, "teams/team_dashboard.html", context)

"""

def my_mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

"""
## do wykresow
class team_dashboard_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        #lol = TeamSummary.objects.order_by('team')
        
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

        x_ave = round(my_mean(off_rtg),2)
        y_ave = round(my_mean(def_rtg),2)

        data2 = {
            'teams': teams,
            'lol': lol,
            'lol2': lol2,
            'reverse_gradient_flag': reverse_gradient_flag,
            'averages': [x_ave, y_ave]
            }
        return Response(data2)
"""



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
