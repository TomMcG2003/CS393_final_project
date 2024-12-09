from django.db import models

# Person
# Team
# Team Stats
# Pitcher
# Batter
# Filder 

# Actor 1
class Person(models.Model):
    person_id       = models.CharField(max_length=50, null=False, primary_key=True)
    firstName       = models.CharField(max_length=50,  null=False)
    lastName        = models.CharField(max_length=50,  null=False)
    birthCity       = models.CharField(max_length=50, null=True)
    birthCountry    = models.CharField(max_length=50, null=True)
    weight          = models.IntegerField(null=True)
    height          = models.IntegerField(null=True)

    def __str__(self):
        return f" {self.firstName} {self.lastName}"
    
    class Meta:
        db_table = 'Person'

class Team(models.Model):
    # get the specific team and the name and the specific franchiseID
    team_id = models.CharField(max_length=50, primary_key=True)
    teamName = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"teamId: {self.team_id} teamName: {self.teamName}"
    
    class Meta:
        db_table = "Team"

class TeamStats(models.Model):
    # year, teamidwinner, teamidloser
    teamstats_id    = models.AutoField(primary_key=True)
    team            = models.ForeignKey(Team, on_delete=models.CASCADE)

    year            = models.IntegerField(null=False)
    wins            = models.IntegerField(null=False)
    losses          = models.IntegerField(null=False)
    rank            = models.IntegerField(null=False)
    divWinner       = models.CharField(max_length=50, null=True)
    wcWinner        = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"TeamStats: {self.team}"
    
    class Meta:
        db_table = "TeamStats"

class Pitching(models.Model):
    pitching_id    = models.AutoField(primary_key=True)
    person         = models.ForeignKey(Person, on_delete=models.CASCADE, null=False)
    team           = models.ForeignKey(Team, on_delete=models.CASCADE, null=False)
    year           = models.IntegerField(null=False)

    wins           = models.IntegerField(null=True)
    loss           = models.IntegerField(null=True)
    games          = models.IntegerField(null=True)
    saves          = models.IntegerField(null=True)
    shutouts       = models.IntegerField(null=True)
    strikeouts     = models.IntegerField(null=True)

    def __str__(self):
        return f"Pitching: {self.person} {self.team}"
    
    class Meta:
        db_table = "Pitching"


class Batting(models.Model):
    batting_id     = models.AutoField(primary_key=True)
    person         = models.ForeignKey(Person, on_delete=models.CASCADE, null=False)
    team           = models.ForeignKey(Team, on_delete=models.CASCADE, null=False)
    year           = models.IntegerField(null=False)

    hits            = models.IntegerField(null=True)
    doubles         = models.IntegerField(null=True)
    triples         = models.IntegerField(null=True)
    homeruns        = models.IntegerField(null=True)
    strikeouts      = models.IntegerField(null=True)
    atbats          = models.IntegerField(null=True)
    def __str__(self):
        return f"Batting: {self.person} {self.team}"
    
    class Meta:
        db_table = "Batting"


class Fielding(models.Model):
    fielding_id     = models.AutoField(primary_key=True) 
    person          = models.ForeignKey(Person, on_delete=models.CASCADE)
    team            = models.ForeignKey(Team, on_delete=models.CASCADE)
    year            = models.IntegerField(null=False)

    putouts         = models.IntegerField(null=True)
    assists         = models.IntegerField(null=True)
    errors          = models.IntegerField(null=True)
    doublePlays     = models.IntegerField(null=True)
    passedBalls     = models.IntegerField(null=True)

    def __str__(self):
        return f"Fielding: {self.person} {self.team}"
    
    class Meta:
        db_table = "Fielding"
