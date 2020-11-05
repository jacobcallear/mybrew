'''Provides functions to handle python lists.'''

from cli import get_input

def swap_lists(dict_of_lists):
    '''Extends 'from-db' list with contents of 'from-user', then clears 'from-user'.
    
    This prevents duplication of rows when reading / writing data.
    '''
    dict_of_lists['from-db'].extend(dict_of_lists['from-user'])
    dict_of_lists['from-user'].clear()

def want_to_overwrite(list_, name='round'):
    '''Checks if user wants to overwrite a populated list.'''
    if list_ != []:
        print(f'A {name} is currently saved, and will be overwritten.')
        overwrite = get_input('"y" to continue, "n" to cancel', bool)
        if not overwrite:
            return False
    return True

def print_lists(*lists, title='', pause=True):
    '''Prints numbered items of lists.'''
    print(f'{title.title()}:')
    i = 0
    empty = True
    for list_ in lists:
        for i, item in enumerate(list_, start = i + 1):
            print(f'  {i}. {item}')
            empty = False
    if empty:
        print('Empty!')
    print()
    if pause:
        input('Hit "enter" to return to menu: ')
