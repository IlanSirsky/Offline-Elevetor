from Elevator import *
from Building import *
from Call import *
import random


class ElevetorExecuter:
    def __init__(self, building, calls):
        self._building = building
        self._elvetors = building.elevators
        self._calls = calls

    def execute(self):
        for call in self._calls:
            elev = self.getBestElevator(call)
            call.SetElevator(elev._id)
            print(elev)

    def getBestElevator(self, call):
        time, src, dst = call.GetData()
        timeToDST = {}
        for elevetor in self._elvetors:
            if (elevetor._state == call._state):
                timeToDST[elevetor] = getTimeToDST(src)
                timeToDST = sorted(timeToDST.values(), key=lambda item: item[1])
        if (timeToDST != {}):
            print(timeToDST)
            elev = list(timeToDST)[0]
            elev.stop(src)
            return elev

        elev = random.choice(self._elvetors)
        elev.stop(src)
        return elev

    def getData(self):
        return self._calls
