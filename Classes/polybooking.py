from  polymorphism import AirbusA319
from airtravel import *


objf = Flights("BA75877",AirbusA319("G-EUPT"))

print(objf.aircraft_model())

print(objf._seating[12]["A"])

objf.allocate_seat("12A","gani")
objf.allocate_seat("13A","bani")
objf.allocate_seat("14C","hani")
objf.allocate_seat("09C","sani")
objf.allocate_seat("08C","pani")
objf.relocate_passenger("12A","15A")
objf.make_boarding_pass(console_card_printer)