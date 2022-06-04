class DataSample:
    datetime = None

    def __init__(self, unitId, consumption, userId, address):
        self.unitId = unitId
        self.consumption = consumption
        self.userId = userId
        self.address = address