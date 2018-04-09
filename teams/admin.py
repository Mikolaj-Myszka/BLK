from django.contrib import admin

# Register your models here.
from .models import TeamClassic
from .models import TeamTeamRebPct



admin.site.register(TeamClassic)
admin.site.register(TeamTeamRebPct)