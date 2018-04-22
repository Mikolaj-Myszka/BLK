from django.db import models



class TeamSummary(models.Model):
	team = models.CharField(max_length=10)
	gp = models.IntegerField()
	
	wins = models.IntegerField()
	at_home = models.IntegerField()
	win_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	team_pts = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	team_poss = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	off_rtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	
	oppo_pts = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	oppo_poss = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	def_rtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	net_rtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	def __str__(self):
		return "Team: " + self.team + " " + str(self.id)





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



class TeamTeamRebPct(models.Model):
	team = models.CharField(max_length=10)
	gp = models.IntegerField()

	ors_m = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	ors_a = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	ors_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	orb_m = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	orb_a = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	orb_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	orf_m = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	orf_a = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	orf_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	drs_m = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	drs_a = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	drs_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	drb_m = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	drb_a = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	drb_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	drf_m = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	drf_a = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	drf_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	ort_m = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	ort_a = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	ort_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	drt_m = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	drt_a = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	drt_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	def __str__(self):
		return "Team: " + self.team + " " + str(self.id)



class TeamTeamPct(models.Model):
	team = models.CharField(max_length=10)
	gp = models.IntegerField()

	ast_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	stl_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	blk_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	tov_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	fls_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	def __str__(self):
		return "Team: " + self.team + " " + str(self.id)



class TeamTeamShotDiv(models.Model):
	team = models.CharField(max_length=10)
	gp = models.IntegerField()

	zero_fgm = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	zero_fga = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	zero_pts = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	zero_ast = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	zero_fg_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	zero_prtg_fga = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	zero_prtg_ast = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	zero_prtg_pts = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	eight_fgm = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	eight_fga = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	eight_pts = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	eight_ast = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	eight_fg_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	eight_prtg_fga = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	eight_prtg_ast = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	eight_prtg_pts = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	sixteen_fgm = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	sixteen_fga = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	sixteen_pts = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	sixteen_ast = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	sixteen_fg_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	sixteen_prtg_fga = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	sixteen_prtg_ast = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	sixteen_prtg_pts = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	three_fgm = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	three_fga = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	three_pts = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	three_ast = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	three_fg_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	three_prtg_fga = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	three_prtg_ast = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	three_prtg_pts = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	def __str__(self):
		return "Team: " + self.team + " " + str(self.id)



class TeamTeamShotAdv(models.Model):
	team = models.CharField(max_length=10)
	gp = models.IntegerField()

	efg_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	ts_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	usg_prtg = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	pps = models.DecimalField(decimal_places=2, max_digits=10, null=True)
	avg_dist = models.DecimalField(decimal_places=2, max_digits=10, null=True)

	def __str__(self):
		return "Team: " + self.team + " " + str(self.id)