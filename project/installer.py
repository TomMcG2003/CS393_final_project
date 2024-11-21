import os
import csv

from final_app.models import Person, Team, Pitching, Batting, Fielding, TeamStats

# Register your models here.

os.environ['GH_TOKEN'] = "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"
csv_base_path = "../lahman_1871-2023_csv"

# the individual row, the specific keys that table accepts, the specific column name in the csv file
def getValue(line, keys, name):
    output = line[keys[name]]
    return output

def generate_key(line):
    key = {}
    for i in range(len(line)):
        key[line[i]] = i
    return key

def doData(fileName, function, count = 0, counthi = 3000):
    with open(f"{csv_base_path}/{fileName}", 'r') as f:
        file = csv.reader(f)
        curCount = count
        key = {}
        for line in file:
            if curCount % 50 == 0:
                print(f"Worked on {curCount}")
            if curCount >= counthi:
                break
            if curCount == 0:
                key = generate_key(line)
            else:
                function(line, key)
            curCount += 1

def filterInt(data):
    if data == '':
        data = None
    else:
        data = int(data)
    return data

## Registering Data into database

def registerPerson(line, keys):
    day = getValue(line, keys, 'birthDay')
    month = getValue(line, keys, "birthMonth")
    year = getValue(line, keys, "birthYear")
    birthDate = f"{year}-{month}-{day}"
    if not (day and month and year):
        birthDate = None
    
    weight = getValue(line, keys, "weight")
    height = getValue(line, keys, "height")

    if weight == '':
        weight = None
    else:
        weight = int(weight)

    if height == '':
        height = None
    else:
        height = int(height)

    newPlayer = Person.objects.create(
            person_id = getValue(line, keys, 'playerID'), 
            birthDay = birthDate,
            firstName = getValue(line, keys, "nameFirst"),
            lastName  = getValue(line, keys, 'nameLast'),
            birthCity = getValue(line, keys, "birthCity"),
            birthCountry = getValue(line, keys, "birthCountry"),
            weight = weight,
            height = height,
        )

def registerBatting(line, keys):
    personId =  getValue(line, keys, 'playerID')
    teamId = getValue(line, keys, 'teamID')

    try:
        batting = Batting.objects.create(
                team = Team.objects.get(team_id = teamId),
                person = Person.objects.get(person_id = personId),
                year = filterInt(getValue(line, keys, 'yearID')),
                
                hits = filterInt(getValue(line, keys, 'H')),
                doubles = filterInt(getValue(line, keys, '2B')),
                triples = filterInt(getValue(line, keys, '3B')),
                homeruns = filterInt(getValue(line, keys, 'H4')),
                strikeouts = filterInt(getValue(line, keys, "SO")),
        )
    except:
        pass 

def registerPitching(line, keys):
    personId =  getValue(line, keys, 'playerID')
    teamId = getValue(line, keys, 'teamID')

    try:
        pitching = Pitching.objects.create(
                team = Team.objects.get(team_id = teamId),
                person = Person.objects.get(person_id = personId),
                year = filterInt(getValue(line, keys, 'yearID')),
                
                wins = filterInt(getValue(line, keys, 'W')),
                loss = filterInt(getValue(line, keys, 'L')),
                games = filterInt(getValue(line, keys, 'G')),
                saves = filterInt(getValue(line, keys, 'SV')),
                shutouts = filterInt(getValue(line, keys, "SHO")),
                strikeouts = filterInt(getValue(line, keys, "SO"))
        )
    except:
        pass


def registerFielding(line, keys):
    personId = getValue(line, keys, 'playerID')
    teamId = getValue(line, keys, 'teamID')

    try:
        fielding = Fielding.objects.create(
                team = Team.objects.get(team_id = teamId),
                person = Person.objects.get(person_id = personId),
                year = filterInt(getValue(line, keys, 'yearID')),
                
                putouts = filterInt(getValue(line, keys, 'PO')),
                assists = filterInt(getValue(line, keys, 'A')),
                errors = filterInt(getValue(line, keys, 'E')),
                doublePlays = filterInt(getValue(line, keys, 'DP')),
                passedBalls = filterInt(getValue(line, keys, 'PB')),
        )
    except:
        pass 

def registerTeams(line, keys):
    teamId = getValue(line, keys, 'teamID'),
    try:
        Team.objects.get(team_id = teamId)
    except:
        team = Team.objects.create(
                team_id = teamId,
                teamName = getValue(line, keys, "name")
            )


def registerTeamStats(line, keys):
    pass


def load(loadSpecific):

    """
    def getIds(line, keys):
        print(line[keys["ID"]])
        
    bt.doData("People.csv", getIds)
    """
    if "person" == loadSpecific or "all" == loadSpecific:
        print("LOADING PERSON TABLE")
        Person.objects.all().delete()
        doData("People.csv", registerPerson, 0, 500)
        print(Person.objects.all())

    if "team" == loadSpecific or "all" == loadSpecific:
        print("LOADING TEAM TABLE")
        Team.objects.all().delete()
        doData("Teams.csv", registerTeams, 0, 400000)
        print(Team.objects.all())

    if "pitch" == loadSpecific or "all" == loadSpecific:
        print("LOADING PITCHING TABLE")
        Pitching.objects.all().delete()
        doData("Pitching.csv", registerPitching, 0, 2000)
        print(Pitching.objects.all())

    if "batting" == loadSpecific or "all" == loadSpecific:
        print("LOADING BATTING TABLE")
        Batting.objects.all().delete()
        doData("Batting.csv", registerBatting, 0, 2000)
        print(Batting.objects.all())
    
    if "fielding" == loadSpecific or "all" == loadSpecific:
        print("LOADING FIELDING TABLE")
        Fielding.objects.all().delete()
        doData("Fielding.csv", registerFielding, 0, 2000)
        print(Fielding.objects.all())
   
