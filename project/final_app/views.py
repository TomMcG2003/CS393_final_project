from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import Hours
from .models import Person, PeopleProfile


# Create your views here.
def index(request):
    return render(request, "final_app/main.html")

def weare(request):
    return render(request, "final_app/weare.html")

def player(request):
    context = {
        'state' : "none"
    }
        
    if request.method == "GET":
        form = PeopleProfile(request.GET)
        if form.is_valid():
            cleanedData = form.cleaned_data
            firstname = cleanedData["firstname"].lower().capitalize()
            lastname = cleanedData["lastname"].lower().capitalize()
            year = cleanedData["yearId"]

            try:
                person =  Person.objects.get(firstName = firstname, lastName = lastname)
            except:
                person = None
            
            if person:
                print(f"firstname is : {firstname} lastname is : {lastname} year is : {year}")
                context['state'] = "found"
                context['Person'] = person
                context['year'] = year
            else:
                context['state'] = "notfound"
    
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





