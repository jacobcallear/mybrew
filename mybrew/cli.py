#! python3
'''Defines functions to get user input and print lists.'''

from collections import namedtuple
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.completion import NestedCompleter

def mybrew_prompt():
    '''Shows mybrew prompt and returns category and option chosen'''
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
    user_input = user_input.split(' ')

    # If invalid input length
    if len(user_input) == 0:
        return None
    if len(user_input) > 2:
        raise NameError('Command not recognised')

    # If valid input length
    try:
        action, table = user_input
    except ValueError:
        action, table = user_input[0], None

    Command = namedtuple('Command', 'action table')
    return Command(action, table)

def ask_for_password():
    '''Get user input while hiding on-screen input with asterisks.'''
    return prompt('Password: ', is_password=True)
        
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
