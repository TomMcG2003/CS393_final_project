from django import forms

class Hours(forms.Form):
    hours_walked = forms.IntegerField(label="Hours Walked", min_value=0, max_value=8)
    date_walked = forms.DateField(label="Date Walked")