class Call:
    id = 1

    UP = 1
    DOWN = -1

    def __init__(self, a, time, src, dst, e, elevator):
        self._a = a
        self._e = e
        self._id = Call.id
        Call.id += 1
        self._time = float(time)
        self._src = int(src)
        self._dst = int(dst)
        self._elevator = int(elevator)
        self._state = Call.UP if self._src < self._dst else Call.DOWN

    def GetTime(self):
        return self._time

    def GetData(self):
        return self._time,self._src,self._dst

    def GetFullData(self):
        data = [self._a,self._time, self._src, self._dst, self._e, self._elevator]
        return data

    def SetElevator(self, elevator):
        self._elevator = elevator

    def GetElevator(self):
        return self._elevator

    def GetState(self):
        return self._state

    def __repr__(self):
        return f"Call id: {self._id}, time: {self._time}, src: {self._src}, dst: {self._dst}\n"
