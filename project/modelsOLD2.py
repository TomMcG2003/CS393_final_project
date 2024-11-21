

"""

class Season(models.Model):
    seasonId    = models.IntegerField(null=False, primary_key=True)
    year        = models.DateField()

    def __str__(self):
        return f"Season Id: {self.seasonId} Year: {self.year}"
    
    class Meta:
        db_table = "Season"

class ManagerStats(models.Model):
    managerId   = models.IntegerField(null=False)
    team = models.CharField(max_length=3)
    wins = models.IntegerField()
    losses = models.IntegerField()
    winsToLossPer = models.FloatField()
    ties = models.IntegerField()
    games = models.IntegerField()
    awards = models.CharField(max_length=255)

    def __str__(self):
        return f"Team Id: {self.seasonId} ManagerId: {self.year}"
    class Meta:
        db_table = "ManagerStats"

class PitcherStats(models.Model):
    pitcherId   = models.IntegerField(null=False)
    wins = models.IntegerField()
    losses = models.IntegerField()
    winsToLossPer = models.FloatField()
    era = models.FloatField()
    games = models.IntegerField()
    gs = models.IntegerField()
    gf = models.IntegerField()
    completeGames = models.IntegerField()
    shutOuts = models.IntegerField()
    saves = models.IntegerField()
    inningsPitched = models.FloatField()
    hits = models.IntegerField()
    runs = models.IntegerField()
    earnedRuns = models.IntegerField()
    homeRuns = models.IntegerField()
    walks = models.IntegerField()  # AKA 'bb'
    intentionalWalks = models.IntegerField()  # AKA 'ibb'
    strikeOuts = models.IntegerField()
    hitByPitch = models.IntegerField()  # AKA 'hbp'
    balk = models.IntegerField()
    wildPitches = models.IntegerField()
    bf = models.IntegerField()
    eraPlus = models.IntegerField()
    fip = models.FloatField()  # AKA fielding independent pitching
    whip = models.FloatField()  # AKA walks and hits per innings pitched
    hitsPerNine = models.FloatField()
    homeRunsPerNine = models.FloatField()
    walksPerNine = models.FloatField()
    strikeOutsPerNine = models.FloatField()
    strikeOutsToWalks = models.FloatField()
    awards = models.CharField(max_length=255)

    def __str__(self):
        return f"Pitcher Id: {self.seasonId}"
    class Meta:
        db_table = "PitcherStats"


class OffensiveStats(models.Model):
    offensiveId   = models.IntegerField(null=False)
    age = models.IntegerField()
    games = models.IntegerField()
    plateApp = models.IntegerField()
    atBats = models.IntegerField()
    runs = models.IntegerField()
    hits = models.IntegerField()
    doubles = models.IntegerField()
    triples = models.IntegerField()
    homeRuns = models.IntegerField()
    rbi = models.FloatField()
    stolenBases = models.IntegerField()
    caughtStealing = models.IntegerField()
    walks = models.IntegerField()
    strikeOuts = models.IntegerField()
    battingAverage = models.FloatField()
    onBasePer = models.FloatField()
    slugging = models.FloatField()
    ops = models.FloatField()
    opsPlus = models.IntegerField()
    tb = models.IntegerField()
    gdp = models.IntegerField()
    hitByPitch = models.IntegerField()
    sh = models.IntegerField()
    sf = models.IntegerField()
    intentionalWalks = models.IntegerField()
    pos = models.CharField(max_length=255)
    awards = models.CharField(max_length=255)
    rOBA = models.FloatField()
    rBatPlus = models.IntegerField()
    baBIP = models.FloatField()
    iso = models.FloatField()
    hrPer = models.FloatField()
    soPer = models.FloatField()
    bbPer = models.FloatField()
    ev = models.FloatField()
    hardHitPer = models.FloatField()
    idPer = models.FloatField()
    bgPer = models.FloatField()
    gbPer = models.FloatField()
    fbPer = models.FloatField()
    gbTofbPer = models.FloatField()  # gb is ground balls, fb is fly balls
    pullPer = models.FloatField()
    centPer = models.FloatField()
    oppoPer = models.FloatField()
    wpa = models.FloatField()
    cWPA = models.FloatField()
    reTwoFour = models.FloatField()
    rsPer = models.FloatField()
    sbPer = models.FloatField()
    xbtPer = models.FloatField()

    def __str__(self):
        return f"Offensive Id: {self.offensiveId}"
    class Meta:
        db_table = "OffensiveStats"


class DefensiveStats(models.Model):
    defensiveId   = models.IntegerField(null=False)
    age = models.IntegerField()
    position = models.CharField(max_length=3)
    games = models.IntegerField()
    gamesStarted = models.IntegerField()
    completeGames = models.IntegerField()
    innings = models.FloatField()
    ch = models.IntegerField()
    po = models.IntegerField()
    a = models.IntegerField()
    errors = models.IntegerField()
    n = models.FloatField()
    fieldingPer = models.FloatField()
    rtot = models.IntegerField()
    rdrs = models.IntegerField()
    rtotPerYear = models.IntegerField()
    rdrsPerYear = models.IntegerField()
    rfPerNine = models.FloatField()
    rfPerGame = models.FloatField()
    lgFLDPer = models.FloatField()
    lgRFGNine = models.FloatField()
    pb = models.IntegerField()
    wp = models.IntegerField()
    sb = models.IntegerField()
    csPer = models.FloatField()
    lgCSPer = models.FloatField()
    po = models.IntegerField()
    awards = models.CharField(max_length=255)

    def __str__(self):
        return f"Defensive Id: {self.defensiveId}"
    class Meta:
        db_table = "DefensiveStats"

class AthleteSeasonPerformance(models.Model):
    athleteSeasonPerformanceId = models.IntegerField()
    seasonId                   = models.ForeignKey(Season, on_delete=models.CASCADE)
    pitcherId              = models.ForeignKey(PitcherStats, on_delete=models.CASCADE)
    defenseId             = models.ForeignKey(DefensiveStats, on_delete=models.CASCADE)
    offensiveId             = models.ForeignKey(OffensiveStats, on_delete=models.CASCADE)

    def __str__(self):
        return f"athleteSeasonPerformanceId: {self.athleteSeasonPerformanceId} \nseasonId: {self.seasonId} \npitcherId: {self.pitcherId} \ndefenseId: {self.defenseId} \noffenseId: {self.offensiveId}"
    class Meta:
        db_table = "AthleteSeasonPerformance"

class ManagerSeasonPerformance(models.Model):
    managerSeasonPerformanceId = models.IntegerField()
    seasonId                   = models.ForeignKey(Season, on_delete=models.CASCADE)
    managerId               = models.ForeignKey(ManagerStats, on_delete=models.CASCADE)

    def __str__(self):
        return f"ManagerSeasonPerformance Id: {self.managerSeasonPerformanceId} seasonId: {self.seasonId}"
    class Meta:
        db_table = "ManagerSeasonPerformance"

class PlayerSeason(models.Model):
    playerSeasonId  = models.CharField(max_length=50, null=False)
    seasonId        = models.ForeignKey(Season, on_delete=models.CASCADE)
    playerId        = models.ForeignKey(Player, on_delete=models.CASCADE)
    age             = models.IntegerField()
    salary          = models.IntegerField(null=False)
    athleteSeasonPerformanceId  =   models.ForeignKey(AthleteSeasonPerformance,  on_delete=models.CASCADE)
    managerSeasonPerformanceId  =   models.ForeignKey(ManagerSeasonPerformance, on_delete=models.CASCADE)

    def __str__(self):
        return f"PlayerSeason Id: {self.playerSeasonId} seasonId: {self.seasonId} playerId: {self.playerId}"
    class Meta:
        db_table = "PlayerSeason"
"""