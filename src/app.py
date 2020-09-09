#! python3
'''Provides interactive menu to create 'rounds' of people associated with drinks.'''
from os import system

from src.classes import Drink, Order, Person, Preference
from src.data_handling import read_classes_from_mysql, write_classes_to_mysql
from src.menu import get_index_input, get_input, print_list, select_option

drinks, people, rounds, preferences = [], [], [], []
# Note whether already read in data - if so, truncate table before writing
# to avoid duplicating rows
read_drinks, read_people, read_rounds, read_preferences = (False for _ in range(4))

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
            drinks.append(Drink(name, volume, hot, fizzy))
        # Print drinks
        elif option == 1:
            print_list('drinks', drinks)
        # Save drinks to MySQL table
        elif option == 2:
            write_classes_to_mysql(drinks, 'drinks',
                                   truncate=read_drinks)
        # Read drinks from MySQL table
        elif option == 3:
            drinks = read_classes_from_mysql(Drink, 'drinks')
            read_drinks = True

    # ==============================
    # PEOPLE
    elif category == 1:
        # Add a person
        if option == 0:
            print('Adding a person:')
            name = get_input("person's name")
            age = get_input(f"{name}'s age in years", int)
            sex = get_input(f"{name}'s sex").lower()
            people.append(Person(name, age, sex))
        # Print people
        elif option == 1:
            print_list('people', people)
        # Save people to MySQL table
        elif option == 2:
            write_classes_to_mysql(people, 'people',
                                   truncate=read_people)
        # Read people from MySQL table
        elif option == 3:
            people = read_classes_from_mysql(Person, 'people')
            read_people = True
    
    # ==============================
    # ROUND
    elif category == 2:
        # Make a round
        if option == 0:
            # Check drinks and people are not empty
            if drinks == []:
                print('Round cannot be created as no drinks are saved.')
                continue
            if people == []:
                print('Round cannot be created as no people are saved.')
                continue
            # Clear rounds after warning
            if rounds != []:
                print('A round is currently saved, and will be overwritten.')
                overwrite = get_input('"y" to continue, "n" to cancel', bool)
                if not overwrite:
                    continue
            rounds = []
            # Loop through people, choose a drink for each
            print_list('drinks', drinks, pause=False)
            for person in people:
                drink = get_index_input(f"{person.name}'s favourite drink",
                                        drinks)
                rounds.append(Order(person, drink))
        # Print rounds
        elif option == 1:
            print_list('round', rounds)
        # Save rounds to MySQL table
        elif option == 2:
            write_classes_to_mysql(rounds, 'rounds',
                                   truncate=read_rounds)
        # Read rounds from MySQL table
        elif option == 3:
            rounds = read_classes_from_mysql(Order, 'rounds')
            read_rounds = True
            
    # ==============================
    # PREFERENCES
    elif category == 3:
        # Add a drink preference for a person
        if option == 0:
            # Check drinks and people are not empty
            if people == []:
                print('Preference cannot be added as no drinks are saved.')
                continue
            if drinks == []:
                print('Preference cannot be added as no people are saved.')
                continue
            print_list('people', people)
            person = get_index_input('a person', people)
            print_list('drinks', drinks, pause=False)
            drink = get_index_input('a drink', drinks)
            preferences.append(Preference(person, drink))
        # Print preferences
        elif option == 1:
            print_list('preferences', preferences)
        elif option == 2:
            write_classes_to_mysql(preferences, 'preferences',
                                   truncate=read_preferences)
        elif option == 3:
            preferences = read_classes_from_mysql(Preference, 'preferences')
            read_preferences = True
            
    #==============================
    # OTHER
    elif category == 4:
        if option == 0:
            system('cls')
        elif option == 1:
            print('Exiting program...')
            break
