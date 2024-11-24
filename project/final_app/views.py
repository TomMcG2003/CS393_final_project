from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, User
from django.db.models import Avg, Count, Sum
from django.http import HttpResponse
from .forms import PeopleProfile, Authy, TeamProfile, AddPlayer, RemovePlayer, AddTeam, RemoveTeam
from .models import Person, Pitching, Batting, Fielding, Team, TeamStats


# Create your views here.
def index(request):
    return render(request, "final_app/main.html")

def weare(request):
    return render(request, "final_app/weare.html")

def player(request):
    context = {
        'state' : "none"
    }
    # https://stackoverflow.com/questions/3782689/submitting-a-hyperlink-by-get-or-post   
    if request.method == "GET":
        form = PeopleProfile(request.GET)
        if form.is_valid():
            cleanedData = form.cleaned_data
            firstname = cleanedData["firstname"].lower().capitalize()
            lastname = cleanedData["lastname"].lower().capitalize()
            year = cleanedData["yearId"]

            try:
                person =  Person.objects.get(firstName = firstname, lastName = lastname)
                print(f"firstname is : {firstname} lastname is : {lastname} year is : {year}")
                context['state'] = "found"
                context['Person'] = person

                if year:
                    print(f"getting year {year}")
                    context['year'] = year
                    context["yearSpecified"] = True

                    try:
                        pitching = Pitching.objects.all().filter(person = person).get(year = year)
                    except:
                        pitching = None

                    try: 
                        batting = Batting.objects.all().filter(person = person).get(year = year)
                    except:
                        batting = None

                    try:
                        fielding = Fielding.objects.all().filter(person = person).get(year = year)
                    except:
                        fielding = None

                    context['stats'] = {
                        'pitching' : pitching,
                        'batting' : batting,
                        'fielding' : fielding
                    }
                else:
                    context["yearSpecified"] = False
                    years = []

                    for job in Pitching.objects.all().filter(person = person):
                        if not (job.year in years):
                            years.append(job.year)
                    
                    for job in Batting.objects.all().filter(person = person):
                        if not (job.year in years):
                            years.append(job.year)

                    for job in Fielding.objects.all().filter(person = person):
                        if not (job.year in years):
                            years.append(job.year)

                    context["years"] = years         
            except:
                context['state'] = "notfound"       
    
    return render(request, "final_app/player.html", context)

def team(request, user_id=0):
    context = {
        'state' : "notvalid" ,
        'showmiss' : False
    }

    if not request.user.is_authenticated:
        return render(request, "final_app/team.html", context)

    context['state'] = "valid"

    if request.method == "GET":
        form = TeamProfile(request.GET)
        if form.is_valid():
            print("form is valid")
            cleanedData = form.cleaned_data
            teamname = cleanedData["teamname"]
            teamyear = cleanedData["yearId"]

            try:
                team = Team.objects.get(teamName = teamname)
                teamStats = TeamStats.objects.filter(team = team)
                context["teamstats"] = teamStats
                context["team"] = team

                context["foundteam"] = True
                context["foundyear"] = False
                
                context["years"] = []
                context["totalWins"] = 0
                context["totalLoss"] = 0
                for stat in teamStats:
                    context["years"].append(stat.year)
                    context["totalWins"] += stat.wins
                    context["totalLoss"] += stat.losses
                try: 
                    if teamyear != None:
                        teamstat = teamStats.get(year = teamyear)
                        context["teamstat"] = teamstat
                        context["foundyear"] = True

                        # maybe have a featrue that gets all of the players for that team for that year and link it? 
                except:
                    context["showmiss"] = "year does not exist for team"
            except:
                context["showmiss"] = "team does not exist"
                context["foundteam"] = False
        else:
            context["showmiss"] = "Season year has wrong input"
            context["foundteam"] = False

    return render(request, "final_app/team.html", context)
        

def loginsite(request):
    context = {
        'state' : "notvalid",
        'actor' : "lowest",
        'game' : False
    }

    if request.user.is_authenticated:

        if request.method == "POST":
            print(request.POST)
            addPlayer = AddPlayer(request.POST)
            removePlayer = RemovePlayer(request.POST)
            addteam = AddTeam(request.POST)
            removeTeam = RemoveTeam(request.POST)

            ## we need to validate a way to check the specific group that the user is in: vip, employee, manager
            ## we can use user.groups to check which group that the user is in but when printing it out it shows None. 
            if addPlayer.is_valid():
                print("addplayer1")
            elif removePlayer.is_valid():
                print("addplayer2")
            elif addteam.is_valid():
                print("addplayer3")
            elif removeTeam.is_valid():
                print("addplayer4")
            else:
                logout(request)
                print("logged out")

            context['state'] = "logged"
            print(request.user.groups)
            
            return render(request, "final_app/loginsite.html", context)
        else:
            context['state'] = "logged"
            return render(request, "final_app/loginsite.html", context)
    
    if request.method == "GET":
        form = Authy(request.GET)

        if form.is_valid():
            
            cleanedData = form.cleaned_data
            name = cleanedData["username"]
            password = cleanedData["password"]
            print(name + " + " + password)
            # check here if it is valid
            user = authenticate(request, username = name, password = password)
            if user:
                login(request, user)
                context["state"] = "valid"
                context["name"] = name
                # if it is valid send out what specifically who it is.
            else:
                context["state"] = "invalid"

    return render(request, "final_app/loginsite.html", context)





