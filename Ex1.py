import sys

from Building import *
from Elevator import *
import json

def ReadJson(building):
    try:
        with open(building, "r+") as f:
            elevetors = []
            my_d = json.load(f)
            minFloor = my_d.get("_minFloor")
            maxFloor = my_d.get("_maxFloor")
            for elevetor in my_d.get("_elevators"):
                elevetors.append(Elevator(elevetor))
            return Building(minFloor, maxFloor, elevetors)


    except IOError as e:
        print(e)


if __name__ == "__main__":
    args = sys.argv[1:]
    BuildingNumber = 4 # 1-5
    path_json = args[0]
    ourBuilding = ReadJson(path_json)
    print(ourBuilding)
    ourBuilding.elevators.sort()
    print(ourBuilding)

