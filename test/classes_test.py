#! python3
'''Test person class

NOTE
    - All test methods must start with `test` to be run.
'''
import pytest

from src.classes import Person, Drink, Order

class TestPerson:
    @pytest.fixture(autouse=True)
    def _set_attrs(self):
        '''Create new person instance for each test.'''
        self._name = 'Fishoh'
        self._age = 98
        self._sex = 'Female'
        self._person = Person(self._name, self._age, self._sex)
    
    def test_set_attrs(self):
        '''Test attributes are set to correctly value and type.'''
        assert self._name == self._person.name
        assert self._age == self._person.age
        assert self._sex == self._person.sex
    
    def test_to_list(self):
        '''Test `to_list()` method.'''
        expected_list = [self._name, self._age, self._sex]
        assert self._person.to_list() == expected_list

    def test_repr(self):
        '''Test repr.'''
        expected_repr = f"{self._name}, {self._age} years old. {self._sex.title()}."
        assert str(self._person) == expected_repr
    
    def test_from_list(self):
        '''Test `from_list()` initialiser.'''
        list_strings = [self._name, self._age, self._sex]
        person_from_strings = Person.from_list(list_strings)
        assert person_from_strings.name == self._name
        assert person_from_strings.age == self._age
        assert person_from_strings.sex == self._sex

class TestDrink:
    '''Tests Drink class.
    Drink(name=str, volume_ml=int/float, hot=bool, fizzy=bool).
    
    NOTE
        - Doesn't test repr.
    '''
    @pytest.fixture(autouse=True)
    def _set_attrs(self):
        '''Create new drink instance for each test.'''
        self._name = 'Fishoh'
        self._volume_ml = 120
        self._hot = 1
        self._fizzy = 0
        self._drink = Drink(self._name, self._volume_ml, self._hot, self._fizzy)
    
    def test_set_attrs(self):
        '''Test attributes are set to correct value and type.'''
        assert self._name == self._drink.name
        assert self._volume_ml == self._drink.volume_ml
        assert self._hot == self._drink.hot
        assert self._fizzy == self._drink.fizzy
    
    def test_to_list(self):
        '''Test `to_list()` method.'''
        expected_list = [self._name, self._volume_ml, self._hot, self._fizzy]
        assert self._drink.to_list() == expected_list
    
    def test_from_list(self):
        '''Test `from_list()` initialiser.'''
        test_list = [self._name, self._volume_ml, self._hot, self._fizzy]
        drink_from_list = Drink.from_list(test_list)
        assert drink_from_list.name == self._name
        assert drink_from_list.volume_ml == self._volume_ml
        assert drink_from_list.hot == self._hot
        assert drink_from_list.fizzy == self._fizzy

class TestOrder:
    '''Tests Order class.
    Order(person=Person(...), drink=Drink(...))
    '''
    @pytest.fixture(autouse=True)
    def _set_attrs(self):
        '''Create new order instance for each test.'''
        self._person = Person('Brohampton', 208, 'female')
        self._drink = Drink('Orange Juice', 500, hot=0, fizzy=0)
        self._order = Order(self._person, self._drink)
    
    def test_set_attrs(self):
        '''Test attributes are set to correct value and type.'''
        # Person == Order.person
        assert self._person.name == self._order.person.name
        assert self._person.age == self._order.person.age
        assert self._person.sex == self._order.person.sex
        # Drink == Order.drink
        assert self._drink.name == self._order.drink.name
        assert self._drink.volume_ml == self._order.drink.volume_ml
        assert self._drink.hot == self._order.drink.hot
        assert self._drink.fizzy == self._order.drink.fizzy
        
    def test_to_list(self):
        '''Test `from_list()` initialiser.'''
        list_strings = [str(i) for i in (
            self._person.name, self._person.age, self._person.sex,
            self._drink.name, self._drink.volume_ml,
            self._drink.hot, self._drink.fizzy
        )]
        order_from_list = Order.from_list(list_strings)
        assert order_from_list.person.name == self._person.name
        assert order_from_list.person.age == self._person.age
        assert order_from_list.person.sex == self._person.sex
        assert order_from_list.drink.name == self._drink.name
        assert order_from_list.drink.volume_ml == self._drink.volume_ml
        assert order_from_list.drink.hot == self._drink.hot
        assert order_from_list.drink.fizzy == self._drink.fizzy