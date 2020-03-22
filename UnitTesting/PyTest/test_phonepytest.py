

class PhoneBook:

    def __init__(self) ->None:
        self.number =None

    def add(self,name , number):
        self.number = number

    def lookup(self , name):
        return self.number

def test_lookup_by_name():
    phonebook = PhoneBook()
    phonebook.add("Bob","1234")
    assert "1234" == phonebook.lookup("Bob")