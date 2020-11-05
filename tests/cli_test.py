#! python3
'''Test `cli` module.'''
from random import randint

import pytest

from mybrew.cli import get_index_input, get_input, select_option

def test_get_input(monkeypatch):
    '''Ensure `get_input` function returns correct type and value.'''
    def inner_test(monkeypatch, user_input, expected_output):
        '''Assert expected output == actual output'''
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
    '''Ensure `get_index_input` function returns correct item from list.
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

def test_get_index_input_error(monkeypatch):
    '''Ensure `get_index_input` raises ValueError for an empty list.'''
    # Arrange
    list_ = []
    user_input = 'meaningless text'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    # Act, assert
    with pytest.raises(ValueError):
        list_ = []
        get_index_input('meaningless text', list_)

def test_select_option(monkeypatch):
    '''Test `select_option` function.'''
    # Arrange
    user_input = '1'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    expected_output = (int(user_input), int(user_input))
    # Act
    actual_output = select_option()
    # Assert
    assert actual_output == expected_output

def test_select_option_error(monkeypatch):
    '''Ensure `select_option` raises ValueError when choice out of range'''
    # Arrange
    user_input = '5'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    # Act, assert
    with pytest.raises(ValueError):
        select_option()