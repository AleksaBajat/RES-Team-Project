from datetime import datetime

class DataSample:
    def __str__(self):
        return "{} {} {} {} {}".format(self.unitId,self.userId,str(self.address),self.consumption, self.datetime)

    def __init__(self, unitId, consumption, userId, address):
        self.unitId = unitId
        self.consumption = consumption
        self.userId = userId
        self.address = address
        self.datetime = datetime.now().strftime("%B")