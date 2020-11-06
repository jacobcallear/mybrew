#! python3
'''Defines classes to describe a person and a drink, and to link the two.

NOTE
- All classes have a `.to_list()` method and a `.from_list()`
  class method. This is essential for the `app.py` program to work!
'''
from mybrew.get_input import get_index_input, get_input

class Person:
    '''Describe a person's name, age, and sex.'''
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __repr__(self):
        return f'{self.name}, {self.age} years old. {self.sex.title()}.'
    
    def to_list(self):
        '''Return list of attributes.'''
        return [self.name, self.age, self.sex]
    
    @classmethod
    def from_list(cls, list_strings):
        '''Initialise class instance from list of 3 attributes.'''
        name, age, sex = list_strings
        return cls(name, int(age), sex)

    @classmethod
    def from_input(cls):
        name = get_input("person's name")
        age = get_input(f"{name}'s age in years", int)
        sex = get_input(f"{name}'s sex").lower()
        return cls(name, age, sex)

class Drink:
    '''Describe a drink's name, volume (ml), temperature, and fizziness.'''
    def __init__(self, name, volume_ml, hot, fizzy):
        self.name = name
        self.volume_ml = volume_ml
        self.hot = hot
        self.fizzy = fizzy
    
    def __repr__(self):
        temperature = 'hot' if self.hot else 'cold'
        fizzy = 'fizzy ' if self.fizzy else ''
        return f'{self.volume_ml} ml of {temperature} {fizzy}{self.name}.'
    
    def to_list(self):
        '''Return list of attributes.'''
        return [self.name, self.volume_ml, int(self.hot), int(self.fizzy)]
    
    @classmethod
    def from_list(cls, list_strings):
        '''Initialise class instance from list of 4 attributes.'''
        name, vol, hot, fizzy = list_strings
        return cls(name, int(vol), hot == True, fizzy == True)

    @classmethod
    def from_input(cls):
        name = get_input('drink name')
        volume = get_input('drink volume (ml)', int)
        hot = get_input('"y" if drink is hot, otherwise "n"', bool)
        fizzy = get_input('"y" if drink is fizzy, otherwise "n"', bool)
        return cls(name, volume, hot, fizzy)

class Order:
    '''Describe one order (person and drink class).'''
    def __init__(self, person, drink):
        self.person = person
        self.drink = drink
    
    def __repr__(self):
        return f'{self.person.name:<15}: {self.drink}'
    
    def to_list(self):
        '''Return list of attributes.'''
        return self.person.to_list() + self.drink.to_list()
    
    @classmethod
    def from_list(cls, list_strings):
        '''Initialise class instance from list of 7 attributes.'''
        return cls(Person.from_list(list_strings[:3]),
                   Drink.from_list(list_strings[3:]))

class Preference(Order):
    '''Describe one preference (person and drink class).'''
    pass
