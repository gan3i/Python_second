from airtravel import Flights, Aircraft,console_card_printer
from pprint import pprint as pp

a = Aircraft("E-GUP","Airbus A319",num_rows=22,num_seats_per_row=4)

print(a.seating_plan())

objf=Flights("SN99999",Aircraft("E-GUP","Airbus A319",num_rows=22,num_seats_per_row=4))

print(objf.aircraft_model())

print(objf._seating[12]["A"])

objf.allocate_seat("12A","gani")
objf.allocate_seat("13A","bani")
objf.allocate_seat("14C","hani")
objf.allocate_seat("09C","sani")
objf.allocate_seat("08C","pani")
objf.relocate_passenger("12A","15A")
# objf.allocate_seat("12A","django")

# print(objf._seating[13]["A"])

# print (objf.available_seats())

objf.make_boarding_pass(console_card_printer)



# pp(objf._seating)
