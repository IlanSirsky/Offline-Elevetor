class Elevator:
    def __init__(self, data):
        self._id = data.get("_id")
        self._speed = data.get("_speed")
        self._minFloor = data.get("_minFloor")
        self._maxFloor = data.get("_maxFloor")
        self._closeTime = data.get("_closeTime")
        self._openTime = data.get("_openTime")
        self._startTime = data.get("_startTime")
        self._stopTime = data.get("_stopTime")

    def __repr__(self):
        return f"ID= {self._id}"

    def __lt__(self, other):
        return self._speed>other._speed

    def getSpeed(self):
        return self._speed

    def getID(self):
        self._id


