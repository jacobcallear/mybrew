import pytest

from mybrew.list_handling import swap_lists, want_to_overwrite, print_lists

def test_swap_lists():
    # Arrange
    example_input = {
        'from-db': [1, 2, 3],
        'from-user': [4, 5, 6]
    }
    expected_output = {
        'from-db': [1, 2, 3, 4, 5, 6],
        'from-user': []
    }
    # Act
    swap_lists(example_input)
    # Assert
    assert example_input == expected_output

@pytest.mark.parametrize('input_list, input_overwrite, expected_output', [
    ([], 'n', True),
    ([], 'y', True),
    (['example'], 'y', True),
    (['example'], 'n', False)
])
def test_want_to_overwrite(monkeypatch, input_list, input_overwrite, expected_output):
    monkeypatch.setattr('builtins.input', lambda _: input_overwrite)
    assert want_to_overwrite(input_list) == expected_output    
