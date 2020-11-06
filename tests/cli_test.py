#! python3
'''Test CLI module.'''
import pytest

from mybrew.cli import is_valid_command, parse_command, print_error

@pytest.mark.parametrize('input_command, expected_output', [
    (['add', 'drink'], True),
    (['print', 'people'], True),
    (['save', 'preferences'], True),
    (['read', 'rounds'], True),
    (['help'], True),
    (['clear'], True),
    (['exit'], True),
    ([''], True),
    (['unrecognised', 'command'], False),
    (['too', 'long', 'command'], False),
    (['add'], False),
    (['print'], False),
    (['save'], False),
    (['read'], False),
    (['unrecognised'], False)
])
def test_is_valid_command(input_command, expected_output):
    assert is_valid_command(input_command) == expected_output

@pytest.mark.parametrize('input_command', [
    ['add', 'drinks'],
    ['print', 'people'],
    ['save', 'preferences'],
    ['read', 'rounds'],
    ['help'],
    ['clear'],
    ['exit'],
])
def test_parse_command(input_command):
    if len(input_command) == 1:
        assert parse_command(input_command) == tuple(input_command + [None])
    else:
        assert parse_command(input_command) == tuple(input_command)
