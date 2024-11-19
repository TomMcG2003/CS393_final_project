from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import Hours
from .models import Player, PlayerProfile


# Create your views here.
def index(request):
    return render(request, "final_app/main.html")

def weare(request):
    return render(request, "final_app/weare.html")

def player(request):
    context = {
        'verified' : False
    }
        
    if request.method == "GET":
        form = PlayerProfile(request.GET)

        if form.is_valid():
            cleanedData = form.cleaned_data
            firstname = cleanedData["firstname"].lower()
            lastname = cleanedData["lastname"].lower()
            year = cleanedData["year"]

            print(f"firstname is : {firstname} lastname is : {lastname} year is : {year}")
            print("Getting information of player")  
            if firstname == "test":
                context["verified"] = True   
    
    return render(request, "final_app/player.html", context)

def team(request, gameID=None):
    context = {}
    if gameID is None:
        print(context)
    else:
        print("Pain")
    return render(request, "final_app/team.html", context)

def login(request, stuff=None):
    context = {}
    return render(request, "final_app/login.html", context)





