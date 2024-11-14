import os
import csv
from pybaseball import schedule_and_record

os.environ['GH_TOKEN'] = "YOUR TOKEN HERE"

csv_base_path = "C:\\Users\\thomas.mcgowan\\Desktop\\CS393_final_project\\lahman_1871-2023_csv\\"

#C:\Users\thomas.mcgowan\Desktop\CS393_final_project\lahman_1871-2023_csv\Managers.csv


def generate_key(line):
    key = {}
    for i in range(len(line)):
        key[line[i]] = i
    return key


def get_managers(year):
    with open(f"{csv_base_path}Managers.csv", 'r') as file:
        newFile = csv.reader(file)
        count = 0
        key = {}
        for line in newFile:
            if count == 0:
                key = generate_key(line)
                count += 1
            else:
                if int(line[key['yearID']]) == year:
                    print(line)
                count += 1


get_managers(2022)
