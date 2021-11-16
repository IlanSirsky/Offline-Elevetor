from Elevator import *

class Building:
    def __init__(self, minFloor, maxFloor, elevators):
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self.elevators = elevators

    def __repr__(self):
        return f"MinFloor: {self._minFloor }\nMaxFloor: {self._maxFloor}\nElevators: {self.elevators}"

