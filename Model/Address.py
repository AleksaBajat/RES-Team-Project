class Address:
    def __str__(self):
        return "{} {} {} {}".format(self.country,self.city,self.street,self.street_number)

    def __init__(self, country,city,street, street_number):
        self.country = country
        self.city = city
        self.street = street
        self.street_number = street_number

    def __eq__(self, other):
        return self.country == other.country and self.city == other.city and self.street == other.street and self.street_number == other.street_number