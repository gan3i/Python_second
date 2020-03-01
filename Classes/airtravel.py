
"""MOdel for aircraft flights"""

class Flights:
    """ A flight with perticular passenger aircraft"""
    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in {number}")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code {number}")

        if number[2:].isdigit() and int(number[2:])<=9999:
            raise ValueError(f"Invalid route number {number}")
        self._number=number#implementation details of an obejct which are not ment for consuption
        #or manipulattion by clinets of the object should be pre-fixed with underscore, it's a widely used convention.
        self._aircraft= aircraft

    
    def number(self):
        return self._number
        

    def airlinecode(self):
        return self._number[:2]


    def aircraft_model(self):
        return self._aircraft.model()


class Aircraft:

    def __init__(self, registartion, model, num_rows, num_seats_per_row):
        self._registration = registartion
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row


    def registartion(self):
        return self._registartion


    def model(self):
        return self._model


    def num_rows(self):
        return self._num_rows


    def num_seats_per_row(self):
        return self._num_seats_per_row


    def seating_plan(self):
        return (range(1,self._num_rows+1),
                "ABCDEFGHJK"[:self._num_seats_per_row])


