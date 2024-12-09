import os
import csv
# from django.contrib.models import User, Group
from final_app.models import Person, Team, Pitching, Batting, Fielding, TeamStats

os.environ['GH_TOKEN'] = "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"
csv_base_path = "../lahman_1871-2023_csv"


def parse_brithday(bday):
    bday = bday.replace("/", "-")
    if len(bday) == 8:
        bday = f"{bday[0:6]}19{bday[6:]}"
    elif len(bday) > 8:
        pass
    else:
        bday = None
    if bday is not None:
        bday = bday.split("-")
        day = int(bday[0])
        month = int(bday[1])
        year = int(bday[2])
        if month > 12:
            temp = day
            day = month
            month = temp
        bday = f"{year}-{month}-{day}"
        # print(bday)
        return bday


def generate_key(line):
    key = {}
    for i in range(len(line)):
        key[line[i]] = i
    print(key)
    return key


reverseTeams = {}
teams = {}


# Works!
def load_people():
    with open(f"{csv_base_path}/People.csv", 'r') as f:
        file = csv.reader(f)
        personIDDict = {}  # This dict will hold the personIDs that we have to generate
        key = {}
        curCount = 0
        for line in file:
            if curCount % 100 == 0:
                print(f"{curCount = }")
            if curCount == 0:
                key = generate_key(line)
                curCount += 1
            else:
                playerID = line[key["playerID"]]  # Null=False
                # birth = parse_brithday(line[key["birth"]])  # Null=True
                birthCity = line[key["birthCity"]]  # Null=True
                birthCountry = line[key["birthCountry"]]  # Null=True
                weight = line[key["weight"]]  # Null=True
                height = line[key["height"]]  # Null=True
                firstName = line[key["nameFirst"]]
                lastName = line[key["nameLast"]]
                if playerID == "":  # We don't have an id, lets us bbrefid
                    # bbrefID
                    playerID = line[key["bbrefID"]]
                    # print(f"trying the bbrefID: {playerID = }")
                if playerID == "":
                    playerID = f"{lastName}{firstName[1:3]}"
                    try:
                        playerID = f"{playerID}{personIDDict[playerID] + 1}"
                        personIDDict[playerID] += 1
                    except KeyError:
                        personIDDict[playerID] = 1
                        playerID = f"{playerID}{personIDDict[playerID]}"
                # if birth == "":
                #     birth = None
                if birthCity == "":
                    birthCity = None
                if birthCountry == "":
                    birthCountry = None
                if weight == "":
                    weight = None
                else:
                    weight = int(weight)
                if height == "":
                    height = None
                else:
                    height = int(height)
                if firstName == "":
                    firstName = "None"
                if lastName == "":
                    lastName = "None"
                # print(f"{playerID=}, {birth=}, {birthCity=}, {birthCountry=}, {weight=}, {height=}")
                try:
                    player = Person.objects.create(person_id=playerID, firstName=firstName, lastName=lastName,
                                                   birthCity=birthCity, birthCountry=birthCountry,
                                                   weight=weight, height=height)
                    player.save()
                except Exception as e:
                    print(f"{playerID = }, {e = }")
                curCount += 1
        print(key)


def parse_team(team):
    # year-league-name
    team = team.split("-")
    return team[2]


def load_batting():
    with open(f"{csv_base_path}/Batting.csv") as f:
        file = csv.reader(f)
        key = {}
        curCount = 0
        for line in file:
            ef = 0
            if curCount % 100 == 0:
                print(f"{curCount = :_}")
            if curCount == 0:
                key = generate_key(line)
                curCount += 1
            elif curCount >= 50000:
                break
            else:
                curCount += 1
                playerID = line[key["playerID"]]
                teamBadID = line[key['team']]  # year-lg-name
                teamID = reverseTeams[teamBadID]  # teams --> {year-lg-name : BH1}
                year = line[key["yearID"]]
                hits = line[key["H"]]
                doubles = line[key["2B"]]
                triples = line[key["3B"]]
                hr = line[key["HR"]]
                ks = line[key["SO"]]
                abs = line[key['AB']]
                player, team = None, None
                try:
                    player = Person.objects.get(person_id=playerID)
                except Exception as e:
                    print(":")
                    ef = 1
                if ef == 0:
                    try:
                        team = Team.objects.get(team_id=teamID)
                    except Team.MultipleObjectsReturned:
                        print("multiple")
                    except Exception as e:
                        print("::")
                        ef = 1
                    if ef == 0:
                        if year == "":
                            year = 2000
                        else:
                            year = int(year)
                        if hits == "":
                            hits = None
                        else:
                            hits = int(hits)
                        if doubles == "":
                            doubles = None
                        else:
                            doubles = int(doubles)
                        if triples == "":
                            triples = None
                        else:
                            triples = int(triples)
                        if hr == "":
                            hr = None
                        else:
                            hr = int(hr)
                        if ks == "":
                            ks = None
                        else:
                            ks = int(ks)
                        try:
                            batter = Batting.objects.create(person=player, team=team, year=year, hits=hits,
                                                            doubles=doubles, triples=triples, homeruns=hr,
                                                            strikeouts=ks, atbats=abs)
                            batter.save()
                        except Exception as e:
                            print(f"{e = }")
                            pass


# Works!
def load_teams():
    with open(f"{csv_base_path}/Teams.csv", 'r') as f:
        file = csv.reader(f)
        key = {}
        # teamDict = {}
        curCount = 0
        for line in file:
            if curCount % 100 == 0:
                print(f"{curCount = }")
            if curCount == 0:
                key = generate_key(line)
                curCount += 1
            else:
                curCount += 1
                # badTeamID = line[key["teamID"]]
                badTeamID = f"{line[key['yearID']]}-{line[key['lgID']]}-{line[key['name']]}"
                teamID = line[key["teamID"]]
                teamName = line[key["name"]]
                year = line[key["yearID"]]
                teams[teamID] = badTeamID
                reverseTeams[badTeamID] = teamID
                # print(teamID)
                if teamID == "" and teamName == "":
                    pass
                elif teamID == "":
                    teamNameSplit = teamName.split(" ")
                    tidBase = f"{teamNameSplit[0][0]}{teamNameSplit[1][0]}"
                    teamID = f"{tidBase}{year}"  # {teamDict[tidBase] + 1}"
                    #  ----
                    teamID = badTeamID
                elif teamName == "":
                    teamName = teamID
                try:
                    print(teamID)
                    Team.objects.get(team_id=teamID)
                except:
                    # team = Team.objects.create(team_id=teamID, teamName=teamName)
                    team = Team.objects.create(team_id=teamID, teamName=teamName)
                    team.save()
                    # print(f"{teamID = }")
                    # teams[badTeamID] = teamID


def load_team_stats():
    with open(f"{csv_base_path}/Teams.csv", 'r') as f:
        file = csv.reader(f)
        keys = {}
        curCount = 0
        # teamID, year, wins, losses, rank, divWinner, wcWinner
        # teamID = <year>-<lg>-<name>
        for line in file:
            if curCount % 100 == 0:
                print(f"{curCount = }")
            if curCount == 0:
                keys = generate_key(line)
                print(keys)
                curCount += 1
            else:
                curCount += 1
                year = line[keys["yearID"]]
                lg = line[keys["lgID"]]
                name = line[keys['name']]
                # teamId = f"{year}-{lg}-{name}"
                print(line[keys[3]])
                print(teams[line[keys[3]]])
                # teamId = line[keys["team"]]
                teamId = ""
                wins = int(line[keys["W"]])
                losses = int(line[keys["L"]])
                rank = int(line[keys["Rank"]])
                divWins = line[keys["DivWin"]]
                wcWins = line[keys["WCWin"]]
                try:
                    team = Team.objects.get(team_id=teamId)
                    try:
                        teamStat = TeamStats.objects.create(
                            team=team,
                            year=year,
                            wins=wins,
                            losses=losses,
                            rank=rank,
                            divWinner=divWins,
                            wcWinner=wcWins
                        )
                        teamStat.save()
                    except Exception as e:
                        print(f"{e = }")
                except Exception as e:
                    print(f"{e = }")


def grab_team_from_bad_id(teamID):
    try:
        return teams[teamID]
    except KeyError:
        return None


def load_pitching():
    with open(f"{csv_base_path}/Pitching.csv", 'r') as f:
        file = csv.reader(f)
        keys = {}
        curCount = 0
        for line in file:
            if curCount % 100 == 0:
                print(f"{curCount = }")
            if curCount == 0:
                keys = generate_key(line)
                curCount += 1
            # person, team, year, wins, loss, games, saves, shutouts, strikeouts
            # We are going to get the person then grab the team that person was on for that year.
            elif curCount > 3700:
                break
            else:
                curCount += 1
                year = int(line[keys["yearID"]])
                wins = int(line[keys["W"]])
                losses = int(line[keys["L"]])
                games = int(line[keys["G"]])
                saves = int(line[keys["SV"]])
                shutouts = int(line[keys["SHO"]])
                ks = int(line[keys["SO"]])
                try:
                    person = Person.objects.get(person_id=line[keys["playerID"]])
                    # teamID = grab_team_from_bad_id(line[keys["teamID"]])
                    teamID = line[keys["teamID"]]
                    team = Team.objects.get(team_id=teamID)
                    if teamID is not None:
                        try:
                            pitcher = Pitching.objects.create(
                                person=person,
                                team=team,
                                year=year,
                                wins=wins,
                                loss=losses,
                                games=games,
                                saves=saves,
                                shutouts=shutouts,
                                strikeouts=ks
                            )
                            pitcher.save()
                        except:
                            pass
                except Exception as e:
                    print(f"{e = }")
                    pass


def load_fielding():
    with open(f"{csv_base_path}/Fielding.csv", 'r') as f:
        file = csv.reader(f)
        keys = {}
        curCount = 0
        for line in file:
            if curCount % 100 == 0:
                print(f"{curCount = }")
            if curCount == 0:
                keys = generate_key(line)
                curCount += 1
            else:
                # person, team, year, putouts, assists, errors, doubleplays, passedballs
                curCount += 1
                personID = line[keys["playerID"]]
                teamID = line[keys["teamID"]]
                year = line[keys["yearID"]]
                if year == "":
                    year = 2000
                else:
                    year = int(year)
                putouts = line[keys["PO"]]
                if putouts == "":
                    putouts = None
                else:
                    putouts = int(putouts)
                assists = line[keys["A"]]
                if assists == "":
                    assists = None
                else:
                    assists = int(assists)
                errors = line[keys["E"]]
                if errors == "":
                    errors = None
                else:
                    errors = int(errors)
                DPs = line[keys["DP"]]
                if DPs == "":
                    DPs = None
                else:
                    DPs = int(DPs)
                PBs = line[keys["PB"]]
                if PBs == "":
                    PBs = None
                else:
                    PBs = int(PBs)
                try:
                    player = Person.objects.get(person_id=personID)
                    team = Team.objects.get(team_id=teamID)  # grab_team_from_bad_id(teamID))
                    fielder = Fielding.objects.create(
                        team=team,
                        person=player,
                        year=year,
                        putouts=putouts,
                        assists=assists,
                        errors=errors,
                        doublePlays=DPs,
                        passedBalls=PBs
                    )
                    fielder.save()
                except Exception as e:
                    print(f"{e = }")
                    pass


def loadPeople():
    print("Loading people")
    Person.objects.all().delete()
    load_people()
    print(Person.objects.all())
    print("Done")


def loadTeam():
    print("Loading teams")
    Team.objects.all().delete()
    load_teams()
    print(Team.objects.all())
    print("Done")


def loadTeamStats():
    print("Loading team stats")
    TeamStats.objects.all().delete()
    load_team_stats()
    print(TeamStats.objects.all())
    print("Done")


def loadPitching():
    print("Loading pitching stats")
    Pitching.objects.all().delete()
    load_pitching()
    print(Pitching.objects.all())
    print("Done")


def loadBatting():
    print("Loading batting stats")
    Batting.objects.all().delete()
    load_batting()
    print(Batting.objects.all())
    print("Done")


def loadFielding():
    print("Loading batting stats")
    Fielding.objects.all().delete()
    load_fielding()
    print(Fielding.objects.all())
    print("Done")


loadPeople()
loadTeam()
loadTeamStats()
# TODO: Error with permissions after curCount = 37900
loadPitching()
# print(Pitching.objects.all())
# print(Team.objects.all())
# print(Team.objects.get(team_id='1961-AL-Los Angeles Angels'))
loadBatting()
# print(Batting.objects.all())
# print(Person.objects.all())
# print(Pitching.objects.all())
loadFielding()
