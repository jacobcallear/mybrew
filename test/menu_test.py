#! python3
'''Tests menu module. Requires user input.'''

from src.menu import get_index_input, get_input, select_option, print_list

def test_get_input(monkeypatch):
    # Arrange
    monkeypatch.setattr('builtins.input', lambda _: '12')
    # Act
    i = get_input('text', int)
    # Assert
    assert i == 12

