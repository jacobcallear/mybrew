#! python3
'''Defines functions to get user input and print lists.'''

from collections import namedtuple

def select_option():
    '''Prints options menu and returns user input as tuple[int].'''
    # Choose category
    print('''
Select a category:
  [0] DRINKS
  [1] PEOPLE
  [2] ROUNDS
  [3] PREFERENCES
  [4] OTHER
''')
    category = get_input('a number', int)
    # Raise error if invalid category
    if category > 4:
        print('INVALID CATEGORY')
        raise ValueError
    # Print options
    if category == 0:
        print('''
Select an option:
  DRINKS
  [0] Add a drink
  [1] Print drinks list
  [2] Save drinks to file
  [3] Read drinks from file
''')
    elif category == 1:
        print('''
Select an option:
  PEOPLE
  [0] Add a person
  [1] Print people list
  [2] Save people to file
  [3] Read people from file
''')
    elif category == 2:
        print('''
Select an option:
  ROUNDS
  [0] Add a round
  [1] Print round
  [2] Save round to file
  [3] Read round from file
''')
    elif category == 3:
        print('''
Select an option:
  PREFERENCES
  [0] Add a preference
  [1] Print preferences
  [2] Save preferences to file
  [3] Read preferences from file
''')
    elif category == 4:
        print('''
Select an option:
  OTHER
  [0] Clear screen
  [1] Exit
''')
    # Get option input as int
    option = get_input('a number', int)
    # Raise error if invalid category + option
    if category < 4 and option > 3 or option == 4 and option > 1:
        print('INVALID OPTION')
        raise ValueError
    # Return chosen category and option
    Selection = namedtuple('Selection', 'category option')
    return Selection(category, option)
        
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

def print_list(title, items, pause=True):
    '''Prints items of a list.'''
    title = title.title()
    if items == []:
        print(f'{title}: empty')
        return
    print(f'{title}:')
    for i, item in enumerate(items, start = 1):
        print(f'  {i}. {item}')
    print()
    if pause:
        input('Hit "enter" to return to menu: ')