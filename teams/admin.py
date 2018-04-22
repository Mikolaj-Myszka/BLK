from django.contrib import admin

# Register your models here.
from .models import TeamClassic
from .models import TeamTeamRebPct
from .models import TeamTeamPct
from .models import TeamTeamShotDiv
from .models import TeamTeamShotAdv
from .models import TeamSummary




admin.site.register(TeamClassic)
admin.site.register(TeamTeamRebPct)
admin.site.register(TeamTeamPct)
admin.site.register(TeamTeamShotDiv)
admin.site.register(TeamTeamShotAdv)
admin.site.register(TeamSummary)

