from phonebook import PhoneBook
import unittest

class PhoneBookTest(unittest.TestCase):

    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add("Bob",1234)
        number = phonebook.lookup("Bob")
        self.assertEqual(1234,number)


# test = PhoneBookTest()

# test.test_lookup_by_name()


        
