# also an example of error being silenced explicitely

import sys 

try:
    import msvcrt# for windows
    def getykey():
        return msvcrt.getch()
except:   
    import tty #for linux
    #code for linux
