from django.shortcuts import render
from django.http import HttpResponse
from .forms import Hours
from .models import HoursLogged, Player


# Create your views here.

def index(request):
    return render(request, "final_app/main.html")
#HttpResponse('hello')

def hours(request):
    print(request)
    print(dir(request))
    if request.method == "POST":
        print(request.POST)
        submittedForm = Hours(request.POST)
        if submittedForm.is_valid():
            newEntry = HoursLogged(
                numHours=submittedForm.cleaned_data['hours_walked']
            )
            newEntry.save()

    newForm = Hours()
    context = {'form': newForm}
    return render(request, "final_app/hours.html", context)


def player(request, playerID=None):
    context = {}
    if playerID is None:
        if request.method == "GET":
            print("Yay")
            context["players"] = Player.playerID
        print(context)
    else:
        context["players"] = Player.playerID == playerID
    return render(request, "final_app/player.html", context)


