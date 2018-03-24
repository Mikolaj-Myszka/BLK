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

from teams.views import team_page, team_list_view, graph_view, get_data, ChartData

urlpatterns = [
	url(r'^teams/', team_page),
	url(r'^teams2/', team_list_view),
	url(r'^graph/', graph_view),
	url(r'^api-data/', get_data),
	url(r'^api-rest-data/', ChartData.as_view()),
    url(r'^admin/', admin.site.urls),
]
