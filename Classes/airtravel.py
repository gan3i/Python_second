
"""Model for aircraft flights"""

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
        rows, seats = self._aircraft.seating_plan()
        self._seating = [{letter:None for letter in seats} for _ in rows] 

    
    def number(self):
        return self._number
        

    def airlinecode(self):
        return self._number[:2]


    def aircraft_model(self):
        return self._aircraft.model()


    def allocate_seat(self,seat, passenger):
        """Allocate a seat to a passenger

        args:
            seat: a seat designator such as "12c" or "12f"
            passenger : name of the passenger

        raises :
            valueerror: is the given seat is unavailable"
        """
        rows,seat_letter = self._aircraft.seating_plan()
        row,letter = self._parse_seat(seat)
        if self._seating[row][row_letter] is not None:
            raise ValueError(f"seat {seat} has already been occupied")

        self._seating[row][row_letter] = passenger


    def _parse_seat(set):
        row_letter = seat[-1]
        if row_letter not in seat_letter:
            raise ValueError(f"Invalid seat letter {row_letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"invalid seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")


    def relocate_passenger(self, from_seat,to_seat):
        """relocate a passnger to a diffrent seat

            args:
                from_seat: the existing seat designation of the 
                        passenger to be moved.
                to_seat : the new seat designator.

        """
        from_row, from_letter = self._parse_seat(from_seat)

        


class Aircraft:

    def __init__(self, registartion, model, num_rows, num_seats_per_row):
        self._registration = registartion
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row


    def registartion(self):
        return self._registration


    def model(self):
        return self._model


    def num_rows(self):
        return self._num_rows


    def num_seats_per_row(self):
        return self._num_seats_per_row


    def seating_plan(self):
        """Returns the seating plan given number of rows and letter"""
        return (range(1,self._num_rows+1),
                "ABCDEFGHJK"[:self._num_seats_per_row])





