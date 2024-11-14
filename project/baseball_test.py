import csv
import os

os.environ["GH_TOKEN"] = "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"
from pybaseball import schedule_and_record

csvFilePath = "C:\\Users\\thomas.mcgowan\\Desktop\\CS393_final_project\\lahman_1871-2023_csv\\"


def make_key(line):
    dictionary = {}
    for i in range(len(line)):
        dictionary[line[i]] = i
    return dictionary

# ==============================


def get_schedule_for_team(year, team):
    return schedule_and_record(year, team)


def grab_managers_year(year):
    with open(f"{csvFilePath}Managers.csv", 'r') as file:
        csvFile = csv.reader(file)
        count = 0
        key = {}  # mapped to {key: index}
        for line in csvFile:
            if count == 0:
                key = make_key(line)
                print(key.keys())
            else:
                if int(line[key["yearID"]]) == year:
                    print(line)
            count += 1


# grab_managers_year(2000)
# print(get_schedule_for_team(2023, "PHI"))
'''
table value => csv value
managerID => playerID
year => yearID
team => teamID
wins => W
losses => L
wtlPercent => ??? (maybe just W/L)
ties => G - (W+L)
games => G
finish => ??? --> Need to double check what this is
wPost => ???
wtlPostPercent => ???
challenges => None
overturned => None
ejections => None
awards => This come from another table
'''