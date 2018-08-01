from django.contrib import admin

# Register your models here.
from .models import PlayerClassic
from .models import PlayerTeamRebPct
from .models import PlayerTeamPct
from .models import PlayerTeamShotDiv
from .models import PlayerTeamShotAdv
"""
from .models import TeamSummary
"""

admin.site.register(PlayerClassic)
admin.site.register(PlayerTeamRebPct)
admin.site.register(PlayerTeamPct)
admin.site.register(PlayerTeamShotDiv)
admin.site.register(PlayerTeamShotAdv)
"""
admin.site.register(TeamSummary)
"""
