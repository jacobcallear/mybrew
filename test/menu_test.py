#! python3
'''Tests menu module. Requires user input.'''
from random import randint

import pytest

from src.menu import get_index_input, get_input, print_lists, select_option

def test_get_input(monkeypatch):
    '''Tests that `get_input()` returns correct type and value.'''
    def inner_test(monkeypatch, user_input, expected_output):
        # Arrange
        monkeypatch.setattr('builtins.input', lambda _: user_input)
        # Act
        actual_output = get_input('meaningless text',
                                  return_type = type(expected_output))
        # Assert
        assert actual_output == expected_output
    # ----------
    # Integer
    inner_test(monkeypatch, '12', expected_output = 12)
    # String
    text = 'LFJ(£*Jfdksfj£F(*J£F'
    inner_test(monkeypatch, text, expected_output = text)
    # Boolean
    inner_test(monkeypatch, 'y', expected_output = True)
    inner_test(monkeypatch, 'n', expected_output = False)

def test_get_index_input(monkeypatch):
    '''Tests `get_index_input` function.
    NB: Returned indexes start from 1, not 0.
    '''
    # Arrange
    list_ = list(range(10))
    user_input = str(randint(0, len(list_) - 1))
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    expected_output = list_[int(user_input) - 1]
    # Act
    actual_output = get_index_input('meaningless text', list_)
    # Assert
    assert actual_output == expected_output
    
    # Test error raising
    with pytest.raises(ValueError):
        list_ = []
        get_index_input('meaningless text', list_)
