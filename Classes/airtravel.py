
"""Model for aircraft flights"""

class Flights:
    """ A flight with perticular passenger aircraft"""
    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in {number}")#class invarients

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
        row,row_letter = self._parse_seat(seat)
        if self._seating[row][row_letter] is not None:
            raise ValueError(f"seat {seat} has already been occupied")

        self._seating[row][row_letter] = passenger


    def _parse_seat(self,seat):
        rows,seat_letter = self._aircraft.seating_plan()
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

        return int(row_text),row_letter



    def relocate_passenger(self, from_seat,to_seat):
        """relocate a passnger to a diffrent seat

            args:
                from_seat: the existing seat designation of the 
                        passenger to be moved.
                to_seat : the new seat designator.

        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat {from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"seat {to_seat} already occupied") 

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None


    def available_seats(self):
        #  return sum(sum(1 for s in row.values() if s is None) 
        #          for row in self._seating if row is not None)
         return sum(sum(1 for s in row.values() if s is None) 
                  for row in self._seating if row is not None)


    def make_boarding_pass(self,card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger,seat,self.number(),self._aircraft.model())



    def _passenger_seats(self):
        """ Returns an iterable series of passenger seating locations"""
        rows,row_seats = self._aircraft.seating_plan()
        for row in rows:
            for seat in row_seats:
                passenger = self._seating[row-1][seat]
                if self._seating[row-1][seat] is not None:
                    yield (passenger, f"{row}{seat}")


def console_card_printer(passenger,seat,flight_number,aircraft):
    output = f"| Name : {passenger}"      \
            f" Flight : {flight_number}" \
            f" Seat : {seat}"            \
            f" Aircraft : {aircraft}"    \
            " |"
    border = "+"+"-" * (len(output)-2) + "+"
    banner = "|" + " " * (len(output)-2) + "|"
    lines = [border,banner,output,banner, border]
    card = "\n".join(lines)
    from pprint import pprint as pp
    print(card)
    print()




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





