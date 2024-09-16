"""
This program is designed to register eligible voters

Requirements:
Ask for necessary information
 - first & last name, age, address, state, country of citizenship, zipcode
If not >= 18 then program stops
All fields must be entered
Continuous error checking
Exit when necessary
Program only continues if the user meets specified criteria
"""
import sys

def votername():
    """ Prompts for user's name """
    while True:
        first_name = input('\nEnter your first name (or press x to exit the program): ').strip()
        if first_name.lower() == 'x':
            print('Exiting the program...')
            sys.exit(0)

        last_name = input('Enter your last name (or press x to exit the program): ').strip()
        if last_name.lower() == 'x':
            print('Exiting the program...')
            sys.exit(0)

        if not first_name or not last_name:
            print('First and last names are required to register.')
            continue
        return first_name, last_name

def voterage():
    """ Prompts the user for their age, validates it, and terminates if not at least 18 """
    while True:
        try:
            age = (input('Enter your age (or press x to exit the program): ').strip())
            if age.lower() == 'x':
                print('Exiting the program...')
                sys.exit(0)
            if not age:
                print('Please enter your age.')
                continue

            age = int(age)
            if age < 18:
                print('You are ineligible to vote.')
                sys.exit(0)
            elif age > 99:
                print('Enter a valid age.')
                continue
            return age
        except ValueError:
            print('Enter a valid number.')
            continue

def citizenship():
    """ Checks for valid U.S. citizenship,
    if user isn't eligible then the program will terminate """
    while True:
        try:
            country = input('Are you a citizen of the United States [Yes/No] ? '
                            '(or press x to exit the program): ').strip()
            if country.lower() == 'x':
                print('Exiting the program...')
                sys.exit(0)
            if not country:
                print('Please answer Yes or No.')
                continue

            if country == 'No':
                print('You are ineligible to vote.')
                sys.exit(0) # Program terminates if voter isn't a U.S. citizen
            if country == 'Yes':
                return country

        except ValueError:
            print('Enter valid answers.')

def voterlocation():
    """ Prompt for address """
    while True:
        try:
            address = input('Enter your address (or press x to exit the program): ').strip()
            if address.lower() == 'x':
                print('Exiting the program...')
                sys.exit(0)
            if not address:
                print('Please enter your address.')
                continue

            state = input('Enter your state (e.g. MD) (or press x to exit the program): ').strip()
            if state.lower() == 'x':
                print('Exiting the program...')
                sys.exit(0)
            if not state:
                print('Please enter your state.')
                continue

            if len(state) != 2 or not state.isalpha():
                print('Please enter a valid 2-letter state abbreviation.')
                continue

            zipcode = input('Enter your zipcode (or press x to exit the program): ').strip()
            if zipcode.lower() == 'x':
                print('Exiting the program...')
                sys.exit(0)
            if not zipcode:
                print('Please enter your zipcode.')
                continue

            if not zipcode.isdigit() or len(zipcode) != 5:
                print('Please enter a valid zipcode.')
                continue
            return address, state, zipcode
        except ValueError:
            print('All fields must be valid.')

def closingstatement(first_name, last_name):
    """ Closing statement to wrap up the program & produce a clean exit """
    print(f'\nThank you, {first_name} {last_name} , '
          f'for using the Python U.S. Voter Registration Program.')
    print('You are eligible to vote.')

def main():
    """ Main program entry point """
    print('Welcome to the Python U.S. Voter Registration Program.')
    first_name, last_name = votername()
    voterage()
    citizenship()
    voterlocation()
    closingstatement(first_name, last_name)

main()
# Created by Alexis Krueger, Aug. 21 2024, CYOP 300 6380
