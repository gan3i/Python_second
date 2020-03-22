

class PhoneBook:

    def __init__(self) ->None:
        self.numbers ={}

    def add(self,name , number):
        self.numbers[name] = number

    def lookup(self , name):
        return self.numbers[name]

    def names(self):
        return set(self.numbers.keys())

# pytest way for setting up test fixtures/setup 
@pytest.fixture
def phonebook():
    phonebook = PhoneBook()
    return phonebook

#dependencies are injected
def test_lookup_by_name(phonebook):
    phonebook.add("Bob","1234")
    assert "1234" == phonebook.lookup("Bob")

def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob","1234")
    phonebook.add("Missing","12345")
    assert phonebook.names() == {"Bob","Missing"}
    assert "Missing" in phonebook.names()

import pytest
def test_phonbook_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")


