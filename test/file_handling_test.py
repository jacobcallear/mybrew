#! python3
'''Test file_handling module for Person class.

NOTE
    - Make sure cwd is 'rounds' module
'''
import pytest

from src.classes import Person, Drink, Order, Preference
from src.file_handling import read_classes_from_csv, write_classes_to_csv

@pytest.fixture
def people():
    return [Person(name, age, sex)
            for name, age, sex in (
                ('Bob', 24, 'male'),
                ('Bill', 234, 'male'),
                ('Jade', 75, 'female')
                )
            ]

@pytest.fixture
def save_path_people():
    return 'test/test_data/person.csv'

def test_write_person(people, save_path_people):
    '''Write list people to csv.'''
    # Act
    write_classes_to_csv(people, save_path_people)
    # Assert in test_read_person()...

def test_read_person(people, save_path_people):
    '''Reads people from csv, checks attributes.'''
    # Arrange
    expected_people = people
    # Act
    actual_people = read_classes_from_csv(Person, save_path_people)
    # Assert
    for actual_person, expected_person in zip(expected_people, actual_people):
        assert actual_person.name == expected_person.name
        assert actual_person.age == expected_person.age
        assert actual_person.sex == expected_person.sex
