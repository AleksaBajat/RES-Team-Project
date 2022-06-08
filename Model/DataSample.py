from datetime import datetime
from typing import overload

class DataSample:
    def __str__(self):
        return "{} {} {} {} {}".format(self.unitId,self.userId,str(self.address),self.consumption, self.datetime)

    def __init__(self, unitId, consumption, userId, address):
        self.unitId = unitId
        self.consumption = consumption
        self.userId = userId
        self.address = address
        self.datetime = datetime.now().strftime("%B")

    def __eq__(self, other):
        return self.unitId == other.unitId and self.userId == other.userId and self.consumption == other.consumption and self.address == other.address and self.datetime == other.datetime