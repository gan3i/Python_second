# obejcts fitnes for use is only determined at runtime, this is in contrast to statically typede languages.

class Aircrafts:

    def available_seats(self):
        rows, seats = self.seating_plan()
        return len(rows)*len(seats)


    def __init__(self,registration):
        self._registration = registration


    def registration(self):
        return self._registration


class AirbusA319(Aircrafts):

    def model(self):
        return "Airbus A319"


    def seating_plan(self):
        return range(1,23),"ABCDEFGH"


class Boeing777(Aircrafts):

    def model(self):
        return "Boeing 777" 


    def seating_plan(self):
        return range(1,23),"ABCDEFGH"