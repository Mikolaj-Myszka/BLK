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

from .views import (home_page_blk, team_classic_shooting, 
                    team_team_reb_prtg, team_team_reb_prtg_API, 
                    team_team_dreb_prtg, team_team_dreb_prtg_API,
                    team_classic_nonshooting, team_classic_nonshooting_API,
                    ChartData) #get_data

urlpatterns = [
    #url(r'^teams/', team_page),
	#url(r'^teams2/', team_list_view),
    url(r'^$', home_page_blk, name='blk_home'),
	url(r'^team-classic-shooting/', team_classic_shooting, name='team_classic_shooting'),
    url(r'^team-classic-nonshooting/', team_classic_nonshooting, name='team_classic_nonshooting'),
    url(r'^team-team-reb-prtg/', team_team_reb_prtg, name='team_team_reb_prtg'),
    url(r'^team-team-dreb-prtg/', team_team_dreb_prtg, name='team_team_dreb_prtg'),
	#url(r'^api-data/', get_data),
	url(r'^api-rest-data/', ChartData.as_view()),
    url(r'^team-classic-nonshooting-api/', team_classic_nonshooting_API.as_view()),
    url(r'^team-team-reb-prtg-api/', team_team_reb_prtg_API.as_view()),
    url(r'^team-team-dreb-prtg-api/', team_team_dreb_prtg_API.as_view()),
]
