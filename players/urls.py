"""blk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

"""
from .views import (home_page_blk, 
                    team_classic_shooting, team_classic_shooting_API,
                    team_classic_nonshooting, team_classic_nonshooting_API,
                    team_team_oreb_prtg, team_team_oreb_prtg_API, 
                    team_team_dreb_prtg, team_team_dreb_prtg_API,
                    team_team_prtg, team_team_prtg_API,
                    team_team_shot_div_0, team_team_shot_div_0_API,
                    team_team_shot_div_8, team_team_shot_div_8_API,
                    team_team_shot_div_16, team_team_shot_div_16_API,
                    team_team_shot_div_3, team_team_shot_div_3_API,
                    team_team_shot_adv, team_team_shot_adv_API,
                    team_summary, team_summary_API,
                    team_dashboard, team_dashboard_API
                    ) #get_data
"""

from .views import player_classic_shooting, player_classic_shooting_API, player_classic_nonshooting, player_classic_nonshooting_API

urlpatterns = [
    #url(r'^teams/', team_page),
	#url(r'^teams2/', team_list_view),
    #url(r'^$', home_page_blk, name='blk_home'),
	url(r'^player-classic-shooting/', player_classic_shooting, name='player_classic_shooting'),
    url(r'^player-classic-nonshooting/', player_classic_nonshooting, name='player_classic_nonshooting'),
 #    url(r'^team-team-oreb-prtg/', team_team_oreb_prtg, name='team_team_oreb_prtg'),
 #    url(r'^team-team-dreb-prtg/', team_team_dreb_prtg, name='team_team_dreb_prtg'),
 #    url(r'^team-team-prtg/', team_team_prtg, name='team_team_prtg'),
 #    url(r'^team-team-shot-div-0/', team_team_shot_div_0, name='team_team_shot_div_0'),
 #    url(r'^team-team-shot-div-8/', team_team_shot_div_8, name='team_team_shot_div_8'),
 #    url(r'^team-team-shot-div-16/', team_team_shot_div_16, name='team_team_shot_div_16'),
 #    url(r'^team-team-shot-div-3/', team_team_shot_div_3, name='team_team_shot_div_3'),
 #    url(r'^team-team-shot-adv/', team_team_shot_adv, name='team_team_shot_adv'),
 #    url(r'^team-summary/', team_summary, name='team_summary'),
 #    url(r'^team-dashboard/', team_dashboard, name='team_dashboard'),
	# #url(r'^api-data/', get_data),
    url(r'^player-classic-shooting-api/', player_classic_shooting_API.as_view()),
    url(r'^player-classic-nonshooting-api/', player_classic_nonshooting_API.as_view()),
 #    url(r'^team-team-oreb-prtg-api/', team_team_oreb_prtg_API.as_view()),
 #    url(r'^team-team-dreb-prtg-api/', team_team_dreb_prtg_API.as_view()),
 #    url(r'^team-team-prtg-api/', team_team_prtg_API.as_view()),
 #    url(r'^team-team-shot-div-0-api/', team_team_shot_div_0_API.as_view()),
 #    url(r'^team-team-shot-div-8-api/', team_team_shot_div_8_API.as_view()),
 #    url(r'^team-team-shot-div-16-api/', team_team_shot_div_16_API.as_view()),
 #    url(r'^team-team-shot-div-3-api/', team_team_shot_div_3_API.as_view()),
 #    url(r'^team-team-shot-adv-api/', team_team_shot_adv_API.as_view()),
 #    url(r'^team-summary-api/', team_summary_API.as_view()),
 #    url(r'^team-dashboard-api/', team_dashboard_API.as_view()),
]
