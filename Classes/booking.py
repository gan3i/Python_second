from airtravel import Flights, Aircraft
from pprint import pprint as pp

a = Aircraft("E-GUP","Airbus A319",num_rows=22,num_seats_per_row=4)

print(a.seating_plan())

objf=Flights("SN99999",Aircraft("E-GUP","Airbus A319",num_rows=22,num_seats_per_row=4))

print(objf.aircraft_model())

print(objf._seating[12]["A"])

objf.allocate_seat("12A","gani")
objf.allocate_seat("12A","gani")
# objf.allocate_seat("12A","django")

print(objf._seating[12]["A"])


# pp(objf._seating)
