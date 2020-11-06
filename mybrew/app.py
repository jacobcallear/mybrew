#! python3
'''Provides interactive menu to create 'rounds' of people associated with drinks.'''
from os import system

from mybrew.classes import Drink, Order, Person, Preference
from mybrew.cli import (ask_for_password, is_valid_command, mybrew_prompt,
                        parse_command, print_error, print_help, print_welcome)
from mybrew.credentials import credentials
from mybrew.data_handling import (are_credentials_valid,
                                  read_classes_from_mysql,
                                  setup_mybrew_database,
                                  write_classes_to_mysql)
from mybrew.get_input import get_index_input
from mybrew.list_handling import print_lists, swap_lists, want_to_overwrite

# Keep separate lists of user-inputted data and data read from database
# This avoids duplicating rows
drinks, people, rounds, preferences = (
    {'from-db': [], 'from-user': []}
    for _ in range(4)
)
rounds = []

# Get password
credentials['password'] = ask_for_password()

if not are_credentials_valid(credentials):
    raise ValueError('''Invalid password or credentials
Ensure correct credentials are stored in mybrew/credentials.json''')

# Ensure mybrew database exists with appropriate tables
setup_mybrew_database(credentials)
credentials['db'] = 'mybrew'

print_welcome()
while True:
    # Get user input
    user_input = mybrew_prompt()
    if user_input == '':
        continue
    if not is_valid_command(user_input):
        print_error(user_input)
        continue
    action, table = parse_command(user_input)

    # ==============================
    if table == 'drinks':
        if action == 'add':
            print('Adding a drink...')
            drink = Drink.from_input()
            drinks['from-user'].append(drink)

        elif action == 'print':
            print_lists(drinks['from-db'], drinks['from-user'],
                       title='drinks', pause=True)

        elif action == 'save':
            write_classes_to_mysql(drinks['from-user'], 'drinks', credentials)
            swap_lists(drinks)

        elif action == 'read':
            drinks['from-db'] = read_classes_from_mysql(Drink, 'drinks', credentials)

    # ==============================
    elif table == 'people':
        if action == 'add':
            print('Adding a person...')
            person = Person.from_input()
            people['from-user'].append(person)

        elif action == 'print':
            print_lists(people['from-db'], people['from-user'],
                        title='people', pause=True)

        elif action == 'save':
            write_classes_to_mysql(people['from-user'], 'people', credentials)
            swap_lists(people)

        elif action == 'read':
            people['from-db'] = read_classes_from_mysql(Person, 'people', credentials)
    
    # ==============================
    elif table == 'rounds':
        if action == 'add':
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
            print('Adding round...')
            print_lists(all_drinks, title='drinks', pause=False)
            for person in all_people:
                drink = get_index_input(f"{person.name}'s favourite drink",
                                        all_drinks)
                rounds.append(Order(person, drink))

        elif action == 'print':
            print_lists(rounds, title='round', pause=True)

        elif action == 'save':
            if not want_to_overwrite(rounds):
                continue
            write_classes_to_mysql(rounds, 'rounds', credentials, truncate=True)

        elif action == 'read':
            if not want_to_overwrite(rounds):
                continue
            rounds = read_classes_from_mysql(Order, 'rounds', credentials)
            
    # ==============================
    elif table == 'preferences':

        if action == 'add':
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

        elif action == 'print':
            print_lists(preferences['from-db'], preferences['from-user'],
                        title='preferences')
        elif action == 'save':
            write_classes_to_mysql(
                preferences['from-user'], 'preferences', credentials
            )
            swap_lists(preferences)
        elif action == 'read':
            preferences['from-db'] = read_classes_from_mysql(
                Preference,'preferences', credentials
            )
            
    #==============================
    elif table == None:
        if action == 'clear':
            system('cls')
        elif action == 'exit':
            print('Exiting program...')
            break
        elif action == 'help':
            print_help()
