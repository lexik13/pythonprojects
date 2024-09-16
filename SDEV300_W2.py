"""
This is a menu-driven Python program that offers math-security solutions.
Requirements:
6 options
a. generate secure password
b. calculate & format a percentage
c. calculate amount of days till 07-04-2025 (July 4th 2025)
d. use law of cosines to calculate the leg of a triangle
e. create the volume of a right circular cylinder
f. exit program
"""

import math
import string
from datetime import datetime
import secrets

def generate_pass():
    """
 creates random secure passwords
 prompts for user's preferred length & complexity level
    """
    try:
        length = int(input('\nEnter desired length for password'
                           ' [Must be at least 8 characters but no more than 20]: '))
        if not 8 <= length <= 20:
            print('Error: Length must be between 8 and 20 characters.')
            return

        # Prompts for password specification
        print('Enter yes or no for the desired password specifications.')
        uppercase_choice = input('Include uppercase letters?: ').strip().lower() == 'yes'
        lowercase_choice = input('Include lowercase letters?: ').strip().lower() == 'yes'
        digits = input('Include digits?: ').strip().lower() == 'yes'
        special_characters = input('Include special characters?: ').strip().lower() == 'yes'

        pass_set = ''
        if uppercase_choice:
            pass_set += string.ascii_uppercase
        if lowercase_choice:
            pass_set += string.ascii_lowercase
        if digits:
            pass_set += string.digits
        if special_characters:
            pass_set += string.punctuation
        if not pass_set:
            print('Error: You must make at least one selection.')
            return

        password = []
        if uppercase_choice:
            password.append(secrets.choice(string.ascii_uppercase))
        if lowercase_choice:
            password.append(secrets.choice(string.ascii_lowercase))
        if digits:
            password.append(secrets.choice(string.digits))
        if special_characters:
            password.append(secrets.choice(string.punctuation))

        password += [secrets.choice(pass_set) for _ in range(length - len(password))]

        secrets.SystemRandom().shuffle(password)

        password = ''.join(password)
        print(f'Password Generated: {password}')
    except ValueError:
        print('Error: Please try again.')

def calc_percentage():
    """
    User is prompted to enter numerator & denominator then asked for decimal points
    Percentage is calculated & printed
    """
    try:
        numerator = float(input('\nEnter numerator: '))
        denominator = float(input('Enter denominator: '))
        if denominator == 0:
            print('Invalid input: Denominator cannot be zero.')
            return

        decimals = int(input('Enter number of decimal points: '))
        if decimals <= 0:
            print('Invalid input: Decimal points cannot be negative.')
            return

        print('Okay, the program will now calculate the percentage...')

        percentage = (numerator / denominator) * 100
        formatted_percentage = f'{percentage:.{decimals}f}%'
        print(formatted_percentage)
    except ValueError:
        print('Invalid input. Non-numeric values are prohibited.')

def calc_time(assigned_date):
    """
    Function calculates the number of days there are until 07-04-2025 (July 4th, 2025)
    """
    today = datetime.now()
    delta = assigned_date - today
    return delta.days

def cosine_law(a_leg, b_leg, gamma):
    """
    Function will calculate the leg of a triangle
    formula: c^2 = a^2 + b^2 - 2ab * cos(gamma)
    gamma = angle between a * b, c is the side opposite gamma
    """
    gamma_radians = math.radians(gamma)
    c_squared = a_leg ** 2 + b_leg ** 2 - 2 * a_leg * b_leg * math.cos(gamma_radians)
    c_cosine = math.sqrt(c_squared)
    return c_cosine

def cylinder_vol(radius_entered, height_entered):
    """
    Calculates the volume of a right circular cylinder
    """
    return math.pi * radius_entered**2 * height_entered

def exit_program():
    """
    Immediately exits the program
    """
    print('Thank you for using the Math & Security Solutions Program.')
    print('Exiting the program...')
    return False

def menu_selection():
    """
    Menu selection
    """

    user_choice = True
    while user_choice: #Menu Loop
        print('\n          The Menu')
        print('a. Generate secure password')
        print('b. Calculate a percentage')
        print('c. Calculate amount of days until July 4, 2025')
        print('d. Use the Law of Cosines to calculate the leg of a triangle')
        print('e. Create the volume of a right circular cylinder')
        print('f. Exit program')
        selection = input('\n      Enter your choice: ')

        if selection == 'a': # if-else selection loop
            generate_pass()

        elif selection == 'b':
            calc_percentage()

        elif selection == 'c':
            assigned_date = datetime(2025, 7, 4)
            days_until = calc_time(assigned_date)
            print(f'There are {days_until} days until July 4th, 2025 ')

        elif selection == 'd':
            a = float(input('\nEnter the length of side a: '))
            b = float(input('Enter the length of side b: '))
            gamma_degrees = int(input('Enter the number of degrees: '))
            c = cosine_law(a, b, gamma_degrees)
            print(f'The leg of a triangle is: {c:.2f}')

        elif selection == 'e': #Cylinder volume: user input & calculated output
            input_radius = float(input('\nEnter the radius of the cylinder: '))
            input_height = float(input('Enter the height of the cylinder: '))
            volume = cylinder_vol(input_radius, input_height)
            print(f'The volume of a right circular cylinder is {volume:.2f}')

        elif selection == 'f':
            user_choice = exit_program()

        else:
            print('Error. Invalid selection.')

def main():
    """ Main Program Entry Point """
    print('Welcome to the Math & Security Python Program.')
    print('This program is designed to offer math & security solutions.')
    menu_selection()

main()

# Created by Alexis Krueger, CYOP 300 6380, Aug. 28 2024 