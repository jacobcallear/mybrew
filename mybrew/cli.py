#! python3
'''Defines functions to parse user commands at prompt.'''

from collections import namedtuple

from prompt_toolkit import print_formatted_text, prompt
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.formatted_text import FormattedText

def mybrew_prompt():
    '''Provides prompt and command auto-completion.
    Returns user input as space-separated list
    '''
    # Define command auto-completion
    table_names = {
        'drinks': None,
        'people': None,
        'preferences': None,
        'rounds': None
    }
    mybrew_completer = NestedCompleter.from_nested_dict({
        'add': {
            'drink': None,
            'person': None,
            'preference': None,
            'round': None
        },
        'print': table_names,
        'save': table_names,
        'read': table_names,
        'clear': None,
        'exit': None
    })
    # Get user input
    user_input = prompt(FormattedText([('#268bd2', 'mybrew> ')]),
                        completer=mybrew_completer)
    return user_input.split(' ')

def is_valid_command(args):
    '''Checks correct number of valid arguments'''
    # If invalid input length
    if len(args) > 2:
        return False
    if len(args) == 1:
        valid_commands = {'clear', 'exit', ''}
        if args[0] in valid_commands:
            return True
        return False
    if args[0] == 'add':
        valid_args = {
            'drink',
            'person',
            'preference',
            'round'
        }
        if args[1] in valid_args:
            return True
        return False
    if args[0] not in {'print', 'save', 'read'}:
        return False
    if args[1] not in {'drinks', 'people', 'preferences', 'rounds'}:
        return False
    return True

def parse_command(command):
    '''Parse list of 1-2 commands into a namedtuple of (action, table)'''
    try:
        action, table = command
    except ValueError:
        action, table = command[0], None
    # Convert singular to plural for add <table> command
    if table == 'drink':
        table = 'drinks'
    elif table == 'person':
        table = 'people'
    elif table == 'preference':
        table = 'preferences'
    elif table == 'round':
        table = 'rounds'
    # Return parsed input
    Command = namedtuple('Command', 'action table')
    return Command(action, table)

def ask_for_password():
    '''Get user input while hiding on-screen input with asterisks.'''
    return prompt('Password: ', is_password=True)

def print_error(commands):
    '''Prints red error message.'''
    error_message = f"ERROR: `{' '.join(commands)}` is not a recognised command`"
    print_formatted_text(FormattedText([('#FF0000', error_message)]))
