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
from .views import (
                    team_summary, team_summary_API,
                    team_dashboard, team_dashboard_API
                    ) #get_data
"""

from .views import (player_classic_shooting, player_classic_shooting_API,
                    player_classic_nonshooting, player_classic_nonshooting_API,
                    player_team_oreb_prtg, player_team_oreb_prtg_API,
                    player_team_dreb_prtg, player_team_dreb_prtg_API,
                    player_team_prtg, player_team_prtg_API,
                    player_team_shot_div_0, player_team_shot_div_0_API,
                    player_team_shot_div_8, player_team_shot_div_8_API,
                    player_team_shot_div_16, player_team_shot_div_16_API,
                    player_team_shot_div_3, player_team_shot_div_3_API,
                    player_team_shot_adv, player_team_shot_adv_API)

urlpatterns = [
    #url(r'^teams/', team_page),
	#url(r'^teams2/', team_list_view),
    #url(r'^$', home_page_blk, name='blk_home'),
	url(r'^player-classic-shooting/', player_classic_shooting, name='player_classic_shooting'),
    url(r'^player-classic-nonshooting/', player_classic_nonshooting, name='player_classic_nonshooting'),
    url(r'^player-team-oreb-prtg/', player_team_oreb_prtg, name='player_team_oreb_prtg'),
    url(r'^player-team-dreb-prtg/', player_team_dreb_prtg, name='player_team_dreb_prtg'),
    url(r'^player-team-prtg/', player_team_prtg, name='player_team_prtg'),
    url(r'^player-team-shot-div-0/', player_team_shot_div_0, name='player_team_shot_div_0'),
    url(r'^player-team-shot-div-8/', player_team_shot_div_8, name='player_team_shot_div_8'),
    url(r'^player-team-shot-div-16/', player_team_shot_div_16, name='player_team_shot_div_16'),
    url(r'^player-team-shot-div-3/', player_team_shot_div_3, name='player_team_shot_div_3'),
    url(r'^player-team-shot-adv/', player_team_shot_adv, name='player_team_shot_adv'),
 #    url(r'^team-summary/', team_summary, name='team_summary'),
 #    url(r'^team-dashboard/', team_dashboard, name='team_dashboard'),
	# #url(r'^api-data/', get_data),
    url(r'^player-classic-shooting-api/', player_classic_shooting_API.as_view()),
    url(r'^player-classic-nonshooting-api/', player_classic_nonshooting_API.as_view()),
    url(r'^player-team-oreb-prtg-api/', player_team_oreb_prtg_API.as_view()),
    url(r'^player-team-dreb-prtg-api/', player_team_dreb_prtg_API.as_view()),
    url(r'^player-team-prtg-api/', player_team_prtg_API.as_view()),
    url(r'^player-team-shot-div-0-api/', player_team_shot_div_0_API.as_view()),
    url(r'^player-team-shot-div-8-api/', player_team_shot_div_8_API.as_view()),
    url(r'^player-team-shot-div-16-api/', player_team_shot_div_16_API.as_view()),
    url(r'^player-team-shot-div-3-api/', player_team_shot_div_3_API.as_view()),
    url(r'^player-team-shot-adv-api/', player_team_shot_adv_API.as_view()),
 #    url(r'^team-summary-api/', team_summary_API.as_view()),
 #    url(r'^team-dashboard-api/', team_dashboard_API.as_view()),
]
