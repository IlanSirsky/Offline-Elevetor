import sys
import csv

from Building import *
from Elevator import *
from Call import *
from ElevetorExecuter import *

import json

def ReadJson(path):

    try:
        with open(path, "r+") as f:
            elevetors = []
            my_d = json.load(f)
            minFloor = int(my_d.get("_minFloor"))
            maxFloor = int(my_d.get("_maxFloor"))
            for elevetor in my_d.get("_elevators"):
                elevetors.append(Elevator(elevetor))
            return Building(minFloor, maxFloor, elevetors)


    except IOError as e:
        print(e)

def ReadCSV(path):
    data = []
    with open(path) as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            call = Call(a=row[0],time=row[1], src=row[2], dst=row[3],e=row[4])
            data.append(call)
    return data

def WriteCSV(path, data_Full):
    data = []
    for datas in data_Full:
        data.append(datas.GetFullData())
    with open(path ,'w+', newline="") as file:
        csvwrite = csv.writer(file)
        csvwrite.writerows(data)


if __name__ == "__main__":
    args = sys.argv[1:]
    path_json = args[0]
    path_csv_input = args[1]
    path_csv_output = args[2]
    callData = ReadCSV(path_csv_input)
    ourBuilding = ReadJson(path_json)
    ourBuilding.elevators.sort() # sort by elevator speed
    execute = ElevetorExecuter(ourBuilding, callData)
    execute.execute()

    WriteCSV(path_csv_output, execute.getData())

