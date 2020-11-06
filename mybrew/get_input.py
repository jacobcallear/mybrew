'''Provides functions to get user input of correct type.

Used in `mybrew.classes`
'''

def get_input(text, return_type=str):
    '''Get user input and convert to desired type.'''
    # Return string
    if return_type is str:
        return input(text).strip()
    # Return True for 'y', False for 'n'
    if return_type is bool:
        while True:
            yes_no = input(text).strip('" ').lower()
            if yes_no == 'y':
                return True
            if yes_no == 'n':
                return False
            print('Please enter "y" or "n"')
    # Return integer
    if return_type is int:
        while True:
            try:
                return int(input(text).strip())
            except ValueError:
                print('Please enter an integer')
    
def get_index_input(text, list_):
    '''Makes sure user enters a valid index (starts from 1).'''
    length = len(list_)
    if length == 0:
        raise ValueError('Empty list')
    while True:
        index = get_input(f'{text} (number from list): ', int)
        if 0 < index <= length:
            return list_[index - 1]
