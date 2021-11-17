from Elevator import *
from Building import *
from Call import *
import random


class ElevetorExecuter:
    def __init__(self, building, calls):
        self._building = building
        self._elvetors = building.elevators
        self._calls = calls

    def execute(self): # main execute function to send best elevators to all of the floor depends on the time
        for call in self._calls:
            self.checkElevetors(call._time)
            elev = self.getBestElevator(call)
            if type(elev) == int:
                call.SetElevator(elev)
            else:
                call.SetElevator(elev._id)

    def checkElevetors(self, time): # check every elevator if it got the dst
        for elevetor in self._elvetors:
            if elevetor.timeInEnd <= time:
                elevetor.finish()

    def getBestElevator(self, call): # calculate the best elevator for the floor
        time, src, dst = call.GetData()

        if call._elevator != -1: # if this call already got an elevator dont try to give a new one
            return call._elevator

        timeToDST = {}
        for elevetor in self._elvetors: # calculate time - from start to end - elevator to src and src to dst
            if elevetor._dst == None:
                timeToDST[elevetor] = elevetor.getTimeToDis(src, dst) +\
                                      elevetor.getTimeToDis(elevetor._currentPosition,dst)
            else:
                timeToDST[elevetor] = elevetor.getTimeToDis(elevetor._dst, src) + elevetor.getTimeToDis(src, dst) + \
                                      elevetor.getTimeToDis(elevetor._currentPosition,dst) + elevetor._timeToFinish

        timeToDST = sorted(timeToDST.items(), key=lambda item: item[1]) # sort the elevators by the time to end

        elev = list(timeToDST[0])[0]
        elev.goto(time, src, dst) # send elevator to dst

        callState = call._state

        # check if there is an option to collect another call on the way
        for nextCall in self._calls[self._calls.index(call)+1:]:

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

            elev.stop()
            nextCall.SetElevator(elev._id)

        elevetor._currentPosition = dst

        return elev

    def getData(self):
        return self._calls
