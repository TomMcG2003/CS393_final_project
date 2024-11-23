from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, User
from django.http import HttpResponse
from .forms import PeopleProfile, Authy
from .models import Person, Pitching, Batting, Fielding


# Create your views here.
def index(request):
    return render(request, "final_app/main.html")

def weare(request):
    return render(request, "final_app/weare.html")

def player(request, playerYearLink = {}):
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
        'state' : "notvalid",
        'actor' : "lowest"
    }

    if request.user.is_authenticated:
        print(request.user)
        context['state'] = "valid"
        return render(request, "final_app/team.html", context)
    else:
        context['state'] = "notvalid"
        return render(request, "final_app/team.html", context)
        

def loginsite(request):
    context = {
        'state' : "notvalid",
        'actor' : "lowest",
        'game' : False
    }

    if request.user.is_authenticated:

        if request.method == "POST":
            logout(request)
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





