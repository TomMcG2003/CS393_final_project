from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, User
from django.db.models import Avg, Count, Sum
from django.http import HttpResponse
from .forms import PeopleProfile, Authy, TeamProfile, AddPlayer, RemovePlayer, AddTeam, RemoveTeam, EditPlayer, EditTeamStat
from .models import Person, Pitching, Batting, Fielding, Team, TeamStats
import random


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
                # Person.objects.all().filter(firstName = firstname, lastName = lastname)
                person =  Person.objects.get(firstName = firstname, lastName = lastname)
                print(f"firstname is : {firstname} lastname is : {lastname} year is : {year}")
                context['state'] = "found"
                context['Person'] = person

                if year:
                    print(f"getting year {year}")
                    context['year'] = year
                    context["yearSpecified"] = True

                    # Handles pitching work
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
                        context["winPercentage"] = (stat.wins / (stat.wins + stat.losses))
                        context["foundyear"] = True

                        # maybe have a featrue that gets all of the players for that team for that year and make it hyper links?
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
        'game' : False,
        'userType' : None,
        'report' : [],
        'playerfield' : ['City', "Country", "Weight", "Height"],
        'teamfield' : ['Wins', "Losses", "Rank", "DivWinner", "WCWinner"]
    }

    if request.user.is_authenticated:
        context['state'] = "logged"

        if request.user.groups.filter(name='employee').exists():
            context["userType"] = "employee"

        if request.user.groups.filter(name='manager').exists():
            context["userType"] = "manager"


        if request.method == "POST":
            addPlayer = AddPlayer(request.POST)
            removePlayer = RemovePlayer(request.POST)
            editPlayer = EditPlayer(request.POST)
            addteam = AddTeam(request.POST)
            removeTeam = RemoveTeam(request.POST)
            editTeamStat = EditTeamStat(request.POST)

            ## we need to validate a way to check the specific group that the user is in: vip, employee, manager
            ## we can use user.groups to check which group that the user is in but when printing it out it shows None. 
            if addPlayer.is_valid():
                if context["userType"] in ["manager", "employee"]:
                    context["reporttype"] = 1
                    try:
                        person = Person.objects.get(
                            firstName = addPlayer.cleaned_data["firstname1"], 
                            lastName = addPlayer.cleaned_data["lastname1"]
                        )
                        context["report"] = "Person already exists"
                    except:
                        Person.objects.create(
                            person_id = addPlayer.cleaned_data["firstname1"] + addPlayer.cleaned_data["lastname1"] + str(random.randint(0, 1000000)),
                            firstName = addPlayer.cleaned_data["firstname1"], 
                            lastName = addPlayer.cleaned_data["lastname1"]
                        )
                        context["report"] = "Person successfully made."
            elif removePlayer.is_valid():
                if context["userType"] in ["manager", "employee"]:
                    context["reporttype"] = 1
                    try:
                        print("attempting")
                        print(removePlayer.cleaned_data["firstname2"])
                        person = Person.objects.get(
                            firstName = removePlayer.cleaned_data["firstname2"], 
                            lastName = removePlayer.cleaned_data["lastname2"]
                        )
                        
                        person.delete()
                        context["report"] = "Person successfully removed."
                    except:
                        context["report"] = "Person does not exists with player name"
            elif editPlayer.is_valid():
                if context["userType"] in ["manager", "employee"]:
                    context["reporttype"] = 1
                    try:
                        person = Person.objects.get(
                            firstName = editPlayer.cleaned_data["firstname"], 
                            lastName = editPlayer.cleaned_data["lastname"]
                        )
                        field = editPlayer.cleaned_data["field"]
                        value = editPlayer.cleaned_data["value"]
                        if field == "City":
                            person.birthCity = value
                        elif field == "Country":
                            person.birthCountry = value
                        elif field == "Height":
                            person.height = int(value)
                        elif field == "Weight": 
                            person.weight = int(value)
                        person.save()

                        context["report"] = "Person successfully edited."
                    except:
                        context["report"] = "Person does not exists with player name"
            elif addteam.is_valid():
                if request.user.groups.filter(name='manager').exists():
                    context["reporttype"] = 2
                    try:
                        team = Team.objects.get(team_id = addteam.cleaned_data["teamkey1"])
                        context["report"] = "Team already exists with team key"
                    except:
                        Team.objects.create(
                            team_id = addteam.cleaned_data["teamkey1"],
                            teamName = addteam.cleaned_data["teamname1"]
                        )
                        context["report"] = "Team successfully made."
            elif removeTeam.is_valid():
                if request.user.groups.filter(name='manager').exists():
                    context["reporttype"] = 2
                    try:
                        team = Team.objects.get(teamName = removeTeam.cleaned_data["teamname2"])
                        team.delete()
                        context["report"] = "Team successfully removed"
                    except:
                        context["report"] = "Team does not exist with team name"
            elif editTeamStat.is_valid():
                if request.user.groups.filter(name='manager').exists():
                    context["reporttype"] = 2
                    teamstat = None
                    team = None

                    try:
                        team = Team.objects.get(teamName = editTeamStat.cleaned_data["teamname"])
                    except:
                        context["report"] = "Unable to find team with team name"
                        return render(request, "final_app/loginsite.html", context)

                    try:
                        teamstat = TeamStats.objects.get(team = team, year = editTeamStat.cleaned_data["year"])
                        context["report"] = "Team stat modified"
                    except:
                        teamstat = TeamStats.objects.create(
                            team = team,
                            year = editTeamStat.cleaned_data["year"],
                            wins = 0,
                            losses = 0,
                            rank = 0,
                            divWinner = "NA",
                            wcWinner = "NA"
                        )
                        context["report"] = "New team stat made with values"
                    field = editTeamStat.cleaned_data["field"]
                    value = editTeamStat.cleaned_data["value"]

                    if field == "Wins":
                        teamstat.wins = int(value) or 0
                    elif field == "Losses":
                        teamstat.losses = int(value) or 0
                    elif field == "Rank":
                        teamstat.rank = int(value) or 0
                    elif field == "DivWinner": 
                        teamstat.divWinner = value or 0
                    elif field == "WCWinner": 
                        teamstat.wcWinner = value or 0
                    teamstat.save()
            else:
                logout(request)
                context['state'] = "unlogged"

            return render(request, "final_app/loginsite.html", context)
        else:
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





