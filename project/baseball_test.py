import os
import csv
from pybaseball import schedule_and_record
from pybaseball import playerid_reverse_lookup
from pybaseball import playerid_lookup
# from pybaseball import people
os.environ['GH_TOKEN'] = "YOUR TOKEN HERE"

csv_base_path = "C:\\Users\\thomas.mcgowan\\Desktop\\CS393_final_project\\lahman_1871-2023_csv\\"

MANAGERREF = 'bbref'
test = playerid_reverse_lookup(["thompro01"], MANAGERREF)
# print(test["name_last"].values[0])
# print(test["name_first"].values[0])

name = test["name_last"].values[0] + ", " + test["name_first"].values[0]


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

        return players


# get_person("thompro01")
# get_managers(2022)
print(get_players())
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