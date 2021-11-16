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
            self.checkElevetors(call._time)
            elev = self.getBestElevator(call)
            if type(elev) == int:
                call.SetElevator(elev)
            else:
                call.SetElevator(elev._id)

    def checkElevetors(self, time):
        for elevetor in self._elvetors:
            if elevetor.timeInEnd <= time:
                elevetor.finish()

    def getBestElevator(self, call):
        time, src, dst = call.GetData()

        if call._elevator != -1: # if this call already got an elevator dont try to give a new one
            return call._elevator

        timeToDST = {}
        for elevetor in self._elvetors:
            if elevetor._dst == None:
                timeToDST[elevetor] = elevetor.getTimeToDis(src, dst) +\
                                      elevetor.getTimeToDis(elevetor._currentPosition,dst)
            else:
                timeToDST[elevetor] = elevetor.getTimeToDis(elevetor._dst, src) + elevetor.getTimeToDis(src, dst) + \
                                      elevetor.getTimeToDis(elevetor._currentPosition,dst) + elevetor._timeToFinish

        timeToDST = sorted(timeToDST.items(), key=lambda item: item[1])

        elev = list(timeToDST[0])[0]
        elev.goto(time, src, dst)

        callState = call._state

        for nextCall in self._calls[self._calls.index(call)+1:]:
            #print(f"test -- {call}\n nextcall --- {nextCall}")

            if nextCall._time > elev.timeInEnd:
                break

            nextCallState = nextCall._state
            if nextCallState != callState :
                continue
            if nextCallState == Call.UP:
                if nextCall._src < src:
                    continue
            else:
                if nextCall._src > src:
                    continue
            timeToNewCall = elevetor.getTimeToDis(elevetor._currentPosition, src) + elevetor.getTimeToDis(src, nextCall._src)

            if timeToNewCall < nextCall._time:
                continue

            print(f"test -- {call} ----- nextcall --- {nextCall}\n state call {callState} new call {nextCallState}")

            elev.stop()
            nextCall.SetElevator(elev._id)

        elevetor._currentPosition = dst

        return elev


    def getData(self):
        return self._calls
