from phonebook import PhoneBook
import pytest


# pytest way for setting up test fixtures/setup 
# pytest --fixtures gives all the list of fixtures 
@pytest.fixture
def phonebook(tmpdir):
    return PhoneBook(tmpdir)


#dependencies are injected
def test_lookup_by_name(phonebook):
    phonebook.add("Bob","1234")
    assert "1234" == phonebook.lookup("Bob")

def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob","1234")
    phonebook.add("Missing","12345")
    assert phonebook.names() == {"Bob","Missing"}
    assert "Missing" in phonebook.names()


def test_phonbook_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")


