from django import forms

class PeopleProfile(forms.Form):
    firstname = forms.CharField(label="firstname", max_length=50)
    lastname = forms.CharField(label="lastname", max_length=50)
    yearId = forms.IntegerField(required=False)

class TeamProfile(forms.Form):
    teamname =  forms.CharField(label="teamname", max_length=50)
    yearId = forms.IntegerField(required=False)

class Authy(forms.Form):
    username = forms.CharField(label="username", max_length=50, required=True)
    password = forms.CharField(label="password", max_length=50, required=True)

class AddPlayer(forms.Form):
    firstname1 = forms.CharField(label="firstname1", max_length=50,  required=True)
    lastname1 = forms.CharField(label="lastname1", max_length=50,  required=True)

class RemovePlayer(forms.Form):
    firstname2 = forms.CharField(label="firstname2", max_length=50,  required=True)
    lastname2 = forms.CharField(label="lastname2", max_length=50,  required=True)

class EditPlayer(forms.Form):
    firstname = forms.CharField(label="firstname", max_length=50,  required=True)
    lastname = forms.CharField(label="lastname", max_length=50,  required=True)
    field = forms.CharField(label="field", max_length=50,  required=True)
    value = forms.CharField(label="value", max_length=50,  required=True)

class AddTeam(forms.Form):
    teamname1 = forms.CharField(label="teamname1", max_length=50,  required=True)
    teamkey1 = forms.CharField(label="teamkey1", max_length=50,  required=True)

class RemoveTeam(forms.Form):
    teamname2 = forms.CharField(label="teamname2", max_length=50,  required=True)

class EditTeamStat(forms.Form):
    teamname = forms.CharField(label="teamname1", max_length=50,  required=True)
    year = forms.IntegerField(label="year", required=True)
    field = forms.CharField(label="field", max_length=50,  required=True)
    value = forms.CharField(label="value", max_length=50,  required=True)

    