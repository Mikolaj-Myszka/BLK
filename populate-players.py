import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'blk.settings')

import django
django.setup()
from players.models import PlayerClassic
from players.models import PlayerTeamRebPct
from players.models import PlayerTeamPct
from players.models import PlayerTeamShotDiv
from players.models import PlayerTeamShotAdv
"""
from teams.models import TeamSummary
"""
import csv


##### 1 switches on, 0 off
player_team_classic_pergame = 0
player_team_reb_pctg_pergame = 0
player_team_pctg_pergame = 0
player_team_shot_div_pergame = 0
player_team_shot_adv_pergame = 1
#player_summary = 0


###################
i = 0
if player_team_classic_pergame == 1:

    with open('PLAYER-TEAM-CLASSIC-PERGAME.txt') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            i = i + 1
            print(i, row['Player'])

            ## https://amittbhardwj.wordpress.com/2015/10/15/django-queryset-update_or_create/
            
            # In this case, if the TeamClassic already exists, its name is updated
            p = PlayerClassic.objects.update_or_create(
                player=row['Player'],
                defaults={
                    'team': row['Team'],
                    'gp': row['GP'],
                    'gs': row['GS'],

                    'two_fgm': row['2FGM'],
                    'two_fgms': row['2FGMS'],
                    'two_prtg': row['2P%'],

                    'three_fgm': row['3FGM'],
                    'three_fgms': row['3FGMS'],
                    'three_prtg': row['3P%'],

                    'ftm': row['FTM'],
                    'ftms': row['FTMS'],
                    'ft_prtg': row['FT%'],

                    'off_reb': row['OR'],
                    'def_reb': row['DR'],
                    'tot_reb': row['TR'],

                    'ast': row['AST'],
                    'stl': row['STL'],
                    'blk': row['BLK'],
                    'to': row['TO'],
                    'fls': row['FLS'],
                    
                    'mi': row['MIN'],
                    'pts': row['PTS'],
                    }
                )
            print(p)


#https://stackoverflow.com/questions/14115318/create-django-model-or-update-if-exists/26286864#26286864



###################
i = 0
if player_team_reb_pctg_pergame == 1:

    with open('PLAYER-TEAM-REB_PCT-PERGAME.txt') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            i = i + 1
            print(i, row['Player'])

            p = PlayerTeamRebPct.objects.update_or_create(
                player=row['Player'],
                defaults={
                    'team': row['Team'],
                    'gp': row['GP'],

                    'ors_m': row['ORS M'],
                    'ors_a': row['ORS A'],
                    'ors_prtg': row['ORS%'],

                    'orb_m': row['ORB M'],
                    'orb_a': row['ORB A'],
                    'orb_prtg': row['ORB%'],
                    
                    'orf_m': row['ORF M'],
                    'orf_a': row['ORF A'],
                    'orf_prtg': row['ORF%'],


                    'drs_m': row['DRS M'],
                    'drs_a': row['DRS A'],
                    'drs_prtg': row['DRS%'],

                    'drb_m': row['DRB M'],
                    'drb_a': row['DRB A'],
                    'drb_prtg': row['DRB%'],
                    
                    'drf_m': row['DRF M'],
                    'drf_a': row['DRF A'],
                    'drf_prtg': row['DRF%'],


                    'ort_m': row['ORT M'],
                    'ort_a': row['ORT A'],
                    'ort_prtg': row['ORT%'],

                    'drt_m': row['DRT M'],
                    'drt_a': row['DRT A'],
                    'drt_prtg': row['DRT%'],
                    }
                )
            print(p)




###################
i = 0
if player_team_pctg_pergame == 1:

    with open('PLAYER-TEAM-PCT-PERGAME.txt') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            i = i + 1
            print(i, row['Player'])

            p = PlayerTeamPct.objects.update_or_create(
                player=row['Player'],
                defaults={
                    'team': row['Team'],
                    'gp': row['GP'],

                    'ast_prtg': row['Ast%'],
                    'stl_prtg': row['Stl%'],
                    'blk_prtg': row['Blk%'],

                    'tov_prtg': row['Tov%'],
                    'fls_prtg': row['Fls%'],
                    }
                )
            print(p)




###################
i = 0
if player_team_shot_div_pergame == 1:

    with open('PLAYER-TEAM-SHOT_DIV-PERGAME.txt') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            i = i + 1
            print(i, row['Player'])

            p = PlayerTeamShotDiv.objects.update_or_create(
                player=row['Player'],
                defaults={
                    'team': row['Team'],
                    'gp': row['GP'],

                    'zero_fgm': row['0FGM'],
                    'zero_fga': row['0FGA'],
                    'zero_pts': row['0PTS'],
                    'zero_ast': row['0AST'],
                    'zero_fg_prtg': row['0FG%'],
                    'zero_prtg_fga': row['0%FGA'],
                    'zero_prtg_ast': row['0%AST'],
                    'zero_prtg_pts': row['0%PTS'],

                    'eight_fgm': row['8FGM'],
                    'eight_fga': row['8FGA'],
                    'eight_pts': row['8PTS'],
                    'eight_ast': row['8AST'],
                    'eight_fg_prtg': row['8FG%'],
                    'eight_prtg_fga': row['8%FGA'],
                    'eight_prtg_ast': row['8%AST'],
                    'eight_prtg_pts': row['8%PTS'],

                    'sixteen_fgm': row['16FGM'],
                    'sixteen_fga': row['16FGA'],
                    'sixteen_pts': row['16PTS'],
                    'sixteen_ast': row['16AST'],
                    'sixteen_fg_prtg': row['16FG%'],
                    'sixteen_prtg_fga': row['16%FGA'],
                    'sixteen_prtg_ast': row['16%AST'],
                    'sixteen_prtg_pts': row['16%PTS'],

                    'three_fgm': row['3PTM'],
                    'three_fga': row['3FGA'],
                    'three_pts': row['3PTS'],
                    'three_ast': row['3AST'],
                    'three_fg_prtg': row['3PT%'],
                    'three_prtg_fga': row['%3FGA'],
                    'three_prtg_ast': row['%3AST'],
                    'three_prtg_pts': row['%3PTS'],
                    }
                )
            print(p)




###################
i = 0
if player_team_shot_adv_pergame == 1:

    with open('PLAYER-TEAM-SHOT_ADV-PERGAME.txt') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            i = i + 1
            print(i, row['Players'])

            p = PlayerTeamShotAdv.objects.update_or_create(
                player=row['Players'],
                defaults={
                    'team': row['Team'],
                    'gp': row['GP'],

                    'efg_prtg': row['eFG%'],
                    'ts_prtg': row['TS%'],
                    'usg_prtg': row['USG%'],

                    'pps': row['PPS'],
                    'avg_dist': row['AVG DIST'],
                    }
                )
            print(p)


"""
###################not corrected
i = 0
if team_summary == 1:

    with open('df.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            i = i + 1
            print(i, row['team'])

            p = TeamSummary.objects.update_or_create(
                team=row['team'],
                defaults={
                    'gp': row['games'],

                    'wins': row['wins'],
                    'at_home': row['at home'],
                    'win_prtg': row['percent'],

                    'team_pts': row['team_pts'],
                    'team_poss': row['team_poss'],
                    'off_rtg': row['off_pts_poss'],

                    'oppo_pts': row['oppo_pts'],
                    'oppo_poss': row['oppo_poss'],
                    'def_rtg': row['def_pts_poss'],

                    'net_rtg': row['diff'],
                    }
                )
            print(p)
"""



