#! python3
'''Provides interactive menu to create 'rounds' of people associated with drinks.'''
from os import system

from mybrew.classes import Drink, Order, Person, Preference
from mybrew.data_handling import read_classes_from_mysql, write_classes_to_mysql
from mybrew.menu import get_index_input, get_input, print_lists, select_option

# FUNCTIONS

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

# APP START

# Keep separate lists of user-inputted data and data read from database
# This avoids duplicating rows
drinks, people, rounds, preferences = (
    {'from-db': [], 'from-user': []}
    for _ in range(4)
)
rounds = []

while True:
    # Choose option
    try:
        category, option = select_option()
    except ValueError:
        continue
    # ==============================
    # DRINKS
    if category == 0:
        # Add a drink
        if option == 0:
            print('Adding a drink:')
            name = get_input('drink name')
            volume = get_input('drink volume (ml)', int)
            hot = get_input('"y" if drink is hot, otherwise "n"', bool)
            fizzy = get_input('"y" if drink is fizzy, otherwise "n"', bool)
            drinks['from-user'].append(Drink(name, volume, hot, fizzy))
        # Print drinks
        elif option == 1:
            print_lists(drinks['from-db'], drinks['from-user'],
                       title='drinks', pause=True)
        # Save drinks to MySQL table
        elif option == 2:
            write_classes_to_mysql(drinks['from-user'], 'drinks')
            swap_lists(drinks)
        # Read drinks from MySQL table
        elif option == 3:
            drinks['from-db'] = read_classes_from_mysql(Drink, 'drinks')

    # ==============================
    # PEOPLE
    elif category == 1:
        # Add a person
        if option == 0:
            print('Adding a person:')
            name = get_input("person's name")
            age = get_input(f"{name}'s age in years", int)
            sex = get_input(f"{name}'s sex").lower()
            people['from-user'].append(Person(name, age, sex))
        # Print people
        elif option == 1:
            print_lists(people['from-db'], people['from-user'],
                        title='people', pause=True)
        # Save people to MySQL table
        elif option == 2:
            write_classes_to_mysql(people['from-user'], 'people')
            swap_lists(people)
        # Read people from MySQL table
        elif option == 3:
            people['from-db'] = read_classes_from_mysql(Person, 'people')
    
    # ==============================
    # ROUND
    elif category == 2:
        # Make a round
        if option == 0:
            # Check drinks and people are not empty
            all_drinks = drinks['from-db'] + drinks['from-user']
            all_people = people['from-db'] + people['from-user']
            if all_drinks == []:
                print('Round cannot be created as no drinks are saved.')
                continue
            if all_people == []:
                print('Round cannot be created as no people are saved.')
                continue
            # Clear rounds after warning
            if not want_to_overwrite(rounds):
                continue
            rounds = []
            # Loop through people, choose a drink for each
            print_lists(all_drinks, title='drinks', pause=False)
            for person in all_people:
                drink = get_index_input(f"{person.name}'s favourite drink",
                                        all_drinks)
                rounds.append(Order(person, drink))
        # Print rounds
        elif option == 1:
            print_lists(rounds, title='round', pause=True)
        # Save rounds to MySQL table - OVERWRITE previous round
        elif option == 2:
            if not want_to_overwrite(rounds):
                continue
            write_classes_to_mysql(rounds, 'rounds', truncate=True)
        # Read rounds from MySQL table
        elif option == 3:
            if not want_to_overwrite(rounds):
                continue
            rounds = read_classes_from_mysql(Order, 'rounds')
            
    # ==============================
    # PREFERENCES
    elif category == 3:
        # Add a drink preference for a person
        if option == 0:
            # Check drinks and people are not empty
            all_drinks = drinks['from-db'] + drinks['from-user']
            all_people = people['from-db'] + people['from-user']
            if all_drinks == []:
                print('Preference cannot be added as no people are saved.')
                continue
            if all_people == []:
                print('Preference cannot be added as no drinks are saved.')
                continue
            print_lists(all_people, title='people', pause=False)
            person = get_index_input('a person', all_people)
            print_lists(all_drinks, title='drinks', pause=False)
            drink = get_index_input('a drink', all_drinks)
            preferences['from-user'].append(Preference(person, drink))
        # Print preferences
        elif option == 1:
            print_lists(preferences['from-db'], preferences['from-user'],
                        title='preferences')
        elif option == 2:
            write_classes_to_mysql(preferences['from-user'],
                                   table='preferences')
            swap_lists(preferences)
        elif option == 3:
            preferences['from-db'] = read_classes_from_mysql(Preference,
                                                             table='preferences')
            
    #==============================
    # OTHER
    elif category == 4:
        if option == 0:
            system('cls')
        elif option == 1:
            print('Exiting program...')
            break