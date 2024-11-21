from django.db import models

class Player(models.Model):
    playerID = models.CharField(max_length=255, null=False)
    firstName = models.CharField(max_length=255, null=False)
    lastName = models.CharField(max_length=255, null=False)
    salary = models.FloatField()


# Create your models here.
class Manager(models.Model):
    managerID = models.CharField(max_length= 255, null=False)
    currentYear = models.DateField(null=False)
    currentTeam = models.CharField(max_length=3)
    firstName = models.CharField(max_length=255, null=False)
    lastName = models.CharField(max_length=255, null=False)
    birthDay = models.DateField()
    # managerStats = models.ForeignKey

class Game(models.Model):
    gameID = models.IntegerField(null=False)
    
    date = models.DateField()
    homeWinner = models.BooleanField()
    homeScore = models.IntegerField()
    awayScore = models.IntegerField()
    innings = models.IntegerField()
    dayGame = models.BooleanField()
    attendance = models.IntegerField()
    cLI = models.FloatField()
    streak = models.IntegerField()
    
class Team(models.Model):
    # teamID = models.ForeignKey()
    currentYear = models.DateField()
    # player = models.ForeignKey()

class Career(models.Model):
    playerID = models.CharField(max_length=255, null=False)


"""

class ManagerStats(models.Model):
    managerID = models.CharField(max_length=255, null=False)
    currentYear = models.DateField(null=False)
    team = models.CharField(max_length=3)
    wins = models.IntegerField()
    losses = models.IntegerField()
    winsToLossPer = models.FloatField()
    ties = models.IntegerField()
    games = models.IntegerField()
    # finish = models.IntegerField()
    # wPost = models.IntegerField()
    # lPost = models.IntegerField()
    # winsToLossPercPost = models.FloatField()
    # challenges = models.IntegerField()
    # overturned = models.IntegerField()
    # overturnedPerc = models.IntegerField()
    # ejections = models.IntegerField()
    awards = models.CharField(max_length=255)


class Player(models.Model):
    playerID = models.CharField(max_length=255, null=False)
    currentYear = models.DateField(null=False)
    firstName = models.CharField(max_length=255, null=False)
    lastName = models.CharField(max_length=255, null=False)
    # currentTeam = models.ForeignKey()
    # offensiveStats = models.ForeignKey()
    # defensiveStats = models.ForeignKey()
    # pitchingStats = models.ForeignKey()
    salary = models.FloatField()
    leauge = models.CharField(max_length=2)


class PitcherStats(models.Model):
    playerID = models.CharField(max_length=255, null=False)
    currentYear = models.DateField(null=False)
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


class OffensiveStats(models.Model):
    playerID = models.CharField(max_length=255, null=False)
    currentYear = models.DateField(null=False)
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


class DefensiveStats(models.Model):
    playerID = models.CharField(max_length=255, null=False)
    currentYear = models.DateField(null=False)
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


class Schedule(models.Model):
    team = models.CharField(max_length=3, null=False)
    currentYear = models.DateField(null=False)
    # game = models.ForeignKey()

"""
