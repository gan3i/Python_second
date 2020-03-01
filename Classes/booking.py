from airtravel import Flights, Aircraft

a = Aircraft("E-GUP","Airbus A319",num_rows=22,num_seats_per_row=4)

print(a.seating_plan())

objf=Flights("SN99999",Aircraft("E-GUP","Airbus A319",num_rows=22,num_seats_per_row=4))

print(objf.aircraft_model())