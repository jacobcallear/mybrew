#! python3
'''Test get_input module.'''
from random import randint

import pytest

from mybrew.get_input import get_index_input, get_input

@pytest.mark.parametrize('user_input, return_type, expected_output', [
    ('LFJ(£*Jfdksfj£F(*J£F', str, 'LFJ(£*Jfdksfj£F(*J£F'),
    ('239578420357892359408', int, 239578420357892359408),
    ('y', bool, True),
    ('n', bool, False)
])
def test_get_input(monkeypatch, user_input, return_type, expected_output):
    '''Ensure `get_input` function returns correct type and value.'''
    # Arrange
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    # Act
    actual_output = get_input('Meaningless string', return_type=return_type)
    # Assert
    assert actual_output == expected_output

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
