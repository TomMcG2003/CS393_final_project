from django import forms

class PeopleProfile(forms.Form):
    firstname = forms.CharField(label="firstname", max_length=50)
    lastname = forms.CharField(label="lastname", max_length=50)
    yearId = forms.IntegerField(required=False)

class Authy(forms.Form):
    username = forms.CharField(label="username", max_length=50)
    password = forms.CharField(label="password", max_length=50)