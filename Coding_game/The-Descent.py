import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.



# game loop
while True:
    mountain_h = []
    n=8
    for i in range(n):
        mountain_h.append(int(input()))  # represents the height of one mountain.

    #if index == 7:
    mountain_sorted = sorted(mountain_h)
    
        
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # The index of the mountain to fire on.
    print(mountain_h.index(mountain_sorted[n-1]))