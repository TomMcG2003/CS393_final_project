import os
import csv
# from pybaseball import schedule_and_record
# from pybaseball import playerid_reverse_lookup
# from pybaseball import playerid_lookup
# from pybaseball import people
from pybaseball import schedule_and_record

os.environ['GH_TOKEN'] = "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"

csv_base_path = "C:\\Users\\thomas.mcgowan\\Desktop\\CS393_final_project\\lahman_1871-2023_csv\\"

MANAGERREF = 'bbref'
# test = playerid_reverse_lookup(["thompro01"], MANAGERREF)
# print(test["name_last"].values[0])
# print(test["name_first"].values[0])

# name = test["name_last"].values[0] + ", " + test["name_first"].values[0]
months = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12'
}


def make_date(year: int, date: str) -> str:
    date = date.split(', ')
    date = date[1].split(' ')
    # The (1)/(2) denote double headers
    # YYY-MM-DD
    if len(date[1]) == 1:
        date[1] = f"0{date[1]}"
    return f"{year}-{months[date[0]]}-{date[1]}"


def get_schedule(year: int, team: str) -> tuple[dict[int, any], list] or tuple[dict[int, any], any]:
    key = {}
    games = []
    sar = schedule_and_record(year, team.upper())
    for value, index in enumerate(sar.keys()):
        # key[value] = index
        key[index] = value
    for game in sar.values:
        game[0] = make_date(year, game[0])
        games.append(game)
    if len(games) > 162:
        return key, games[0:162]
    return key, games
    # return key, sar.values[0:162]


def generate_key(line):
    key = {}
    for i in range(len(line)):
        key[line[i]] = i
    return key


def get_person(playerID):
    """
    This function will access the data and grab information for a specific person.
    This can be useful if we want to add a specific player/manager into the database.
    """

    with open(f"{csv_base_path}People.csv", 'r') as f:
        file = csv.reader(f)
        count = 0
        key = {}
        for line in file:
            if count == 0:
                count += 1
                key = generate_key(line)
                print(key.keys())
            else:
                if line[key['playerID']] == playerID:
                    print(line)
                count += 1


def get_managers(year=None):
    """
    This function gets the data for all managers in a given year.
    """
    managers = []
    with open(f"{csv_base_path}Managers.csv", 'r') as file:
        newFile = csv.reader(file)
        count = 0
        key = {}
        for line in newFile:
            if count == 0:
                key = generate_key(line)
                managers.append(key)
                count += 1
            else:
                if year is None:
                    managers.append(line)
                else:
                    if int(line[key['yearID']]) == year:
                        managers.append(line)
                count += 1
        return managers


def get_players():
    """
    This function returns all players and their associated stats
    """
    players = []
    with open(f"{csv_base_path}People.csv", 'r') as file:
        f = csv.reader(file)
        count = 0
        key = {}
        for line in f:
            if count == 0:
                key = generate_key(line)
                players.append(key)
                count += 1
            else:
                players.append(list(line[1:]))
            count += 1

        managers = get_managers()
        for player in players:
            if list(player)[0] in managers:
                players.remove(player)
        print(key)
        return players


def batting_per_player(playerID, year=None):
    with open(f"{csv_base_path}Batting.csv", 'r') as file:
        f = csv.reader(file)
        count = 0
        key = {}
        batting = []
        for line in f:
            if count == 0:
                key = generate_key(line)
                # batting.append(key)
                count += 1
            else:
                if playerID == line[0]:
                    if year is None:
                        batting.append(line)
                    else:
                        if str(line[key['yearID']]) == str(year):
                            batting.append(line)
        return batting


def fielding_per_player(playerID, year=None):
    stats = []
    with open(f"{csv_base_path}Fielding.csv", 'r') as file:
        f = csv.reader(file)
        count = 0
        key = {}
        for line in f:
            if count == 0:
                key = generate_key(line)
                count += 1
            if line[0] == playerID:
                if year is None:
                    stats.append(line)
                elif str(year) == line[1]:
                    stats.append(line)
        return key, stats


def pitching_stats(playerID, year=None):
    stats = []
    with open(f"{csv_base_path}Pitching.csv", 'r') as file:
        f = csv.reader(file)
        count = 0
        key = {}
        for line in f:
            if count == 0:
                key = generate_key(line)
                count += 1
            if line[0] == playerID:
                if year is None:
                    stats.append(line)
                elif str(year) == line[1]:
                    stats.append(line)
        return key, stats


def team_roster(year, team):
    roster = []
    with open(f"{csv_base_path}Appearances.csv", 'r') as file:
        f = csv.reader(file)
        for app in f:
            if app[0] == str(year) and app[1] == str(team):
                roster.append(app[3:])
    return roster


# get_person("thompro01")
# print(get_managers(2022))
# get_players()
# print(batting_per_player('aardsda01', 2006))
# key, values = get_schedule(2008, "PHI")
# team_roster(1982, "PHI")
# key, stat = fielding_per_player("aaronha01", 1968)
# key, stat = pitching_stats('abadfe01', 2015)

"""
Info needed for manager stats:
managerID => playerID
year => yearID
team => teamID
wins => W
losses => L
wtlpercent => Not quite sure yet
ties => G - (W+L)
games => G
finish ==> ???
wPost ==> ???
lPost ==> ???
wtlPostPercent ==> ???
challenges ==> ???
overturned ==> ???
overturnPercent ==> ???
ejections ==> ???
awards ==> Another table
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Info needed for Manager:
managerID => managerID
year => yearID
currentTeam => teamID
firstName ==> playerID_reverse_lookup
lastName ==> playerID_reverse_lookup
birthDay ==> Get from People.csv
managerStats ==> foreign key
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Info needed for Player:
playerID => playerID
year => yearID
firstName => playerID_reverse_lookup
lastName => playerID_reverse_lookup
currentTeam => TBD but will be a foreign key
offenseStats => TBD but will be a foreign key
defenseStats => TBD but will be a foreign key
pitcherStats => TBD but will be a foreign key with null option
salary ==> Need to get from Salaries.csv
career ==> TBD but will be a foreign key
"""
