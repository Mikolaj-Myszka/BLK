from django.db import models

class TeamClassic(models.Model):
	team = models.CharField(max_length=10)
	gp = models.IntegerField()

	two_fgm = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	two_fgms = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	two_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	three_fgm = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	three_fgms = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	three_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	ftm = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	ftms = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	ft_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	off_reb = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	def_reb = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	tot_reb = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	ast = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	stl = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	blk = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	to = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	fls = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	mi = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	pts = models.DecimalField(decimal_places=2, max_digits=10, null=True)


	def __str__(self):
		return "Team: " + self.team + " " + str(self.id)



"""
No	Team	GP		2FGM	2FGMS	2P%	3FGM	3FGMS	3P%	
FTM	FTMS	FT%	OR	DR	TR	AST	STL	BLK	TO	FLS	SEC	MIN	PTS	GS	TmREB	TmTO	TmFLS
"""