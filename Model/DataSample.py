from datetime import datetime


class DataSample:
    def __str__(self):
        return "{} {} {} {} {}".format(self.unit_id, self.user_id, str(self.address), self.consumption, self.datetime)

    def __init__(self, unit_id, consumption, user_id, address):
        self.unit_id = unit_id
        self.consumption = consumption
        self.user_id = user_id
        self.address = address
        self.datetime = datetime.now().strftime("%B")

    def __eq__(self, other):
        return self.unit_id == other.unit_id and self.user_id == other.user_id and self.consumption == other.consumption and self.address == other.address and self.datetime == other.datetime