from django import forms

class PeopleProfile(forms.Form):
    firstname = forms.CharField(label="firstname", max_length=50)
    lastname = forms.CharField(label="lastname", max_length=50)
    yearId = forms.IntegerField(required=False)

class TeamProfile(forms.Form):
    teamname =  forms.CharField(label="teamname", max_length=50)
    yearId = forms.IntegerField(required=False)

class Authy(forms.Form):
    username = forms.CharField(label="username", max_length=50)
    password = forms.CharField(label="password", max_length=50)

class Authy2(forms.Form):
    type = forms.CharField(label="type", max_length=50)
    data1 = forms.CharField(label="data1", max_length=50)
    data2 = forms.CharField(label="data2", max_length=50)
    password = forms.CharField(label="password", max_length=50)