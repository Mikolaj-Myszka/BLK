from django.contrib import admin

# Register your models here.
from .models import TeamClassic
from .models import TeamTeamRebPct
from .models import TeamTeamPct
from .models import TeamTeamShotDiv
from .models import TeamTeamShotAdv




admin.site.register(TeamClassic)
admin.site.register(TeamTeamRebPct)
admin.site.register(TeamTeamPct)
admin.site.register(TeamTeamShotDiv)
admin.site.register(TeamTeamShotAdv)
