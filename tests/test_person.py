import pytest
from beings import Person

@pytest.fixture()
def person():
    return Person("Juan Perez", 20, jobs=["Software Engineer"])

def test_init(person: Person):
    assert person.name == "Juan Perez"
    assert person.age == 20
    assert person.jobs == ["Software Engineer"]
    
def test_forname(person: Person):
    assert person.forename == "Juan"
    
def test_surname(person: Person):
    assert person.surname == "Perez"
    
def test_celebreate_birthday(person: Person):
    person.celebrate_birthday()
    assert person.age == 21
    
def test_add_job(person: Person):
    person.add_job("Zookeeper")
    assert person.jobs == ["Software Engineer","Zookeeper"]