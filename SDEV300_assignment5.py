"""
Program allows users to loan one of two CSV files to perform data/statistical analysis

Requirements:
-Prompts user to choose file
-Allows user to perform statistical analysis
-Includes histogram
"""
import pandas as pd
import matplotlib.pyplot as plt


def pop_data():
    """
Function specifically for pop_change.csv
Allows user to choose specific column & perform statistical analysis on it
Should allow user to exit loop and return to main menu
    """
    df_1 = pd.read_csv('PopChange.csv')
    print('You have entered the file: Population Data')
    print('Select the Column you want to analyze:')
    pop_choice = True
    while pop_choice: # Menu Loop for stat analysis
        print('a. Pop April 1')
        print('b. Pop July 1')
        print('c. Change Pop')
        print('d. Exit')
        selection = input('Enter your choice: ')

        if selection == 'a': #If - else loop for choices
            print('You have selected option a.')
            # describe() is used to summarize data in files
            describe_a = df_1['Pop Apr 1'].describe()
            print(describe_a)
            # generating & displaying histogram
            plt.hist(df_1['Pop Apr 1'], bins=30, color='blue', edgecolor='black')
            plt.show()
        elif selection == 'b':
            print('You have selected option b.')
            describe_b = df_1['Pop Jul 1'].describe()
            print(describe_b)
            plt.hist(df_1['Pop Jul 1'], bins=30, color='blue', edgecolor='black')
            plt.show()
        elif selection == 'c':
            print('You have selected option c.')
            describe_c = df_1['Change Pop'].describe()
            print(describe_c)
            # generating & displaying histogram
            plt.hist(df_1['Change Pop'], bins=30, color='blue', edgecolor='black')
            plt.show()
        elif selection == 'd':
            print('Returning to main menu')
            menu_selection()
        else:
            print('Invalid Input.')

def housing_data():
    """
    Function specifically for housing_data.csv
    Columns: age, bedrms, built, rooms, utility
    """
    df_2 = pd.read_csv('Housing.csv')
    print('You have entered the file: Housing Data')
    print('\nSelect the Column you want to analyze:')
    housing_choice = True
    while housing_choice:
        print('a. Age')
        print('b. Bedrooms')
        print('c. Built')
        print('d. Rooms')
        print('e. Utility')
        print('f. Exit')
        selection = input('\nEnter your choice: ')

        if selection == 'a':
            print('You have selected column: Age.')
            describe_1 = df_2['AGE'].describe()
            print(describe_1)
            plt.hist(df_2['AGE'], bins=30, color='blue', edgecolor='black')
            plt.show()
        elif selection == 'b':
            print('You have selected column: Bedrooms.')
            describe_2 = df_2['BEDRMS'].describe()
            print(describe_2)
            plt.hist(df_2['BEDRMS'], bins=30, color='blue', edgecolor='black')
            plt.show()
        elif selection == 'c':
            print('You have selected column: Built.')
            describe_3 = df_2['BUILT'].describe()
            print(describe_3)
            plt.hist(df_2['BUILT'], bins=30, color='blue', edgecolor='black')
            plt.show()
        elif selection == 'd':
            print('You have selected column: Rooms.')
            describe_4 = df_2['ROOMS'].describe()
            print(describe_4)
            plt.hist(df_2['ROOMS'], bins=30, color='blue', edgecolor='black')
            plt.show()
        elif selection == 'e':
            print('You have selected column: Utility.')
            describe_5 = df_2['UTILITY'].describe()
            print(describe_5)
            plt.hist(df_2['AGE'], bins=30, color='blue', edgecolor='black')
            plt.show()
        elif selection == 'f':
            print('Returning to main menu')
            menu_selection()
        else: print('Invalid Input.')

def exit_program():
    """
    Immediately exits the program
    """
    print('Exiting the program...')
    exit()

def menu_selection():
    """
    Allows user to choose file & perform statistical analysis
    """

    user_choice = True
    while user_choice:  # Menu Loop
        print("\n      Select the file you want to analyze: ")
        print('1. Population Data')
        print('2. Housing Data')
        print('3. Exit program')
        selection = input('\n      Enter your choice: ')

        if selection == '1':
            pop_data()
        elif selection == '2':
            housing_data()
        elif selection == '3':
            exit_program()
        else:
            print('Error. Invalid selection.')

def main():
    """
    Main program entry point
    """
    print('Welcome to the Python Data Analysis Program')
    menu_selection()

main()
# Created by Alexis Krueger, Sep. 18th 2024, CYOP 300 6380
