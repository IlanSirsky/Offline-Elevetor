class Elevator:

    UP = 1
    IDLE = 0
    DOWN = -1

    def __init__(self, data):
        self._id = data.get("_id")
        self._speed = float(data.get("_speed"))
        self._minFloor = float(data.get("_minFloor"))
        self._maxFloor = float(data.get("_maxFloor"))
        self._closeTime = float(data.get("_closeTime"))
        self._openTime = float(data.get("_openTime"))
        self._startTime = float(data.get("_startTime"))
        self._stopTime = float(data.get("_stopTime"))
        self._currentPosition = 0
        self._dst = None
        self._src = None
        self._state = Elevator.IDLE
        self._timeToFinish = 0
        self.timeInEnd = 0

    def __repr__(self):
        return f"ID= {self._id}"

    def __lt__(self, other):
        return self._speed>other._speed

    def getSpeed(self):
        return self._speed

    def getFloorTime(self):
        return 1/self._speed

    def getTimeToDis(self, src, dst):
        return self.getFloorTime() * (abs(src - dst)) + self._openTime + self._startTime + self._stopTime + self._closeTime

    def goto(self, time, src, dst):
        self._timeToFinish += self.getTimeToDis(self._currentPosition, src) +  self.getTimeToDis(src, dst)
        self._dst = dst
        self._src = src
        self._state = Elevator.UP if src < dst else Elevator.DOWN
        self.timeInEnd = time + self._timeToFinish

    def stop(self):
        self._timeToFinish += self._openTime + self._startTime + self._stopTime + self._closeTime
        self.timeInEnd += self._openTime + self._startTime + self._stopTime + self._closeTime

    def finish(self):
        self._state = Elevator.IDLE
        self._currentPosition = 0
        self._dst = None
        self._src = None
        self._timeToFinish = 0

    def getID(self):
        return self._id


