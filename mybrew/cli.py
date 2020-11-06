#! python3
'''Defines functions to get user input and print lists.'''

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
        table = 'round'
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

def get_input(text, return_type=str):
    '''Get user input and convert to desired type.'''
    def strip_input(text):
        return input(f'Enter {text}: ').strip()
    # ----------
    # Return string
    if return_type is str:
        return strip_input(text)
    # Return True for 'y', False for 'n'
    if return_type is bool:
        while True:
            yes_no = strip_input(text).strip('" ').lower()
            if yes_no == 'y':
                return True
            if yes_no == 'n':
                return False
            print('Please enter "y" or "n"')
    # Return integer
    if return_type is int:
        while True:
            try:
                return int(strip_input(text))
            except ValueError:
                print('Please enter an integer')
    
def get_index_input(text, list_):
    '''Makes sure user enters a valid index (starts from 1).'''
    length = len(list_)
    if length == 0:
        raise ValueError('Empty list')
    while True:
        index = get_input(f'{text} (number from list)', int)
        if 0 < index <= length:
            return list_[index - 1]
