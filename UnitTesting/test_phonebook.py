from phonebook import PhoneBook
import unittest

class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:#called before every test method
        self.phonebook =PhoneBook()

    def tearDown(self) -> None:#called after every test method
        pass

    def test_lookup_by_name(self):
        self.phonebook.add("Bob",1234)
        number = self.phonebook.lookup("Bob")
        self.assertEqual(1234,number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
           self.phonebook.lookup("Bob")

    # @unittest.skip("WIP")
    def test_empty_phone_book_isconsistent(self):
        self.phonebook = PhoneBook()
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob",'1234')
        self.phonebook.add("Anna",'01234')
        self.assertTrue(self.phonebook.is_consistent)

    def test_inconsistent_with_duplicate_entries(self):
        self.phonebook.add("Bob",'1234')
        self.phonebook.add("sue","1234")
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add("sue","123")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_adds_name_and_number(self):
        self.phonebook.add("Bob","12345")
        self.assertIn("Bob",self.phonebook.get_name())
        self.assertIn("12345", self.phonebook.get_number())


        
