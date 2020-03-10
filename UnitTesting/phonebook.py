

class PhoneBook():  

    def __init__(self):
        self.number = {}
    
    def add(self, name, number):
        self.number[name] = number

    def lookup(self,name):
        return self.number[name]

    def is_consistent(self):
        for name,number in self.number.items():
            for name1, number2 in self.number.items():
                if name == name1:
                    return False
                if number.startswith(number2):
                    return False
        return True

    def get_name(self):
        return (x for x,_ in self.number.items())

    def get_number(self):
        return (x for _,x in self.number.items())
