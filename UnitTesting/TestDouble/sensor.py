

class Sensor():

    def __init__(self):
        self._pressure =0

    
    @property
    def sample_pressure(self):
        return self._pressure