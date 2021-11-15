class Elevator:

    UP = 1
    IDLE = 0
    DOWN = -1

    def __init__(self, data):
        self._id = data.get("_id")
        self._speed = data.get("_speed")
        self._minFloor = data.get("_minFloor")
        self._maxFloor = data.get("_maxFloor")
        self._closeTime = data.get("_closeTime")
        self._openTime = data.get("_openTime")
        self._startTime = data.get("_startTime")
        self._stopTime = data.get("_stopTime")
        self._currentPosition = 0
        self._dst = 0
        self._state = Elevator.IDLE
        self._timeToFinish = 0

    def __repr__(self):
        return f"ID= {self._id}"

    def __lt__(self, other):
        return self._speed>other._speed

    def getSpeed(self):
        return self._speed

    def getFloorTime(self):
        return 1/self._speed

    def getTimeToDST(self, dst):
        return GetFloorTime(self) * (abs(self._currentPosition - dst)) + self._openTime + self._startTime + self._stopTime + self._closeTime

    def goto(self, dst):
        self._timeToFinish = getTimeToDST(dst)
        self._dst = dst
        self._state = Elevator.UP if self._currentPosition < dst else Elevator.DOWN

    def stop(self, dst):
        self._timeToFinish += self._openTime + self._startTime + self._stopTime + self._closeTime
        self._dst = dst

    def finish(self):
        self._state = Elevator.IDLE
        self._currentPosition = self._dst
        self._dst = null
        self._timeToFinish = 0

    def getID(self):
        return self._id


