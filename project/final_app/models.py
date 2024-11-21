from django.db import models
from django import forms

class PeopleProfile(forms.Form):
    firstname = forms.CharField(label="firstname", max_length=50)
    lastname = forms.CharField(label="lastname", max_length=50)
    yearId = forms.IntegerField(required=False)

class Authy(forms.Form):
    username = forms.CharField(label="username", max_length=50)
    password = forms.CharField(label="password", max_length=50)

# Actor 1
class Person(models.Model):
    person_id       = models.CharField(max_length=50, null=False, primary_key=True)
    firstName       = models.CharField(max_length=50,  null=False)
    lastName        = models.CharField(max_length=50,  null=False)
    birthDay        = models.DateField(null=True)
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
        return f"TeamObject teamId: {self.team_id}"
    
    class Meta:
        db_table = "Team"

class TeamStats(models.Model):
    # year, teamidwinner, teamidloser
    teamstats_id    = models.AutoField(primary_key=True)
    team            = models.ForeignKey(Team, on_delete=models.CASCADE)

    year            = models.IntegerField(null=False)
    wins            = models.IntegerField(null=False)
    losses          = models.IntegerField(null=False)
    divWinner       = models.CharField(max_length=50, null=True)
    wcWinner        = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"TeamStats teamID: {self.team}"
    
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
        return f"{self.pitching_id}"
    
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

    def __str__(self):
        return f"{self.batting_id} {self.hits} {self.doubles}"
    
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
        return f"{self.fielding_id}"
    
    class Meta:
        db_table = "Fielding"
