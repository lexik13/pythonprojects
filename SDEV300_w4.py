"""
Matrix game

Algorithm:
1. User enters phone number
2. User enters zip-code(+4)
3. User enters values of 2
4. Program prompts a 3x3 matrix
5. User responds with matrix of choice (???)
6. Repeat 4 & 5 again
7. Program displays matrix operations in a list
8. User selects choice
9. Program returns choice
10. Program stops when user enters N (for No)

"""
import re
import numpy as np

def print_format(matrix):
    """
    Function for formatting the matrix output
    """
    for row in matrix:
        print(' '.join(map(str, row)))

def get_row(row_number):
    """
    Helper function to get a valid row input from the user
    """
    while True:
        try:
            row_input = input(f'Enter integers for row {row_number} : ').strip().split()
            if len(row_input) != 3:
                print('Error. Please enter exactly 3 integers.')
                continue
            row = [int(x) for x in row_input]
            return row
        except ValueError:
            print('Error. Please enter only integers.')

def user_prompts():
    """
    User prompts for phone number & zip-code
    """
    phone_number = None
    zipcode = None
    while phone_number is None:
        phone_number_input = input('Enter phone number: ')
        if (re.fullmatch(r'\d{10}', phone_number_input) or
                re.fullmatch(r'\d{3}-\d{3}-\d{4}', phone_number_input)):
            phone_number = phone_number_input
        else:
            print('Invalid Input. Phone number should be 10 digits.')

    while zipcode is None:
        zipcode_input = input('Enter zip code: ')
        if re.fullmatch(r'\d{5}(-\d{4})?', zipcode_input):
            zipcode = zipcode_input
        else:
            print('Please enter a valid zip code in +4 format (XXXXX-XXXX).')

    matrix_a, matrix_b = user_matrices()
    matrices_menu(matrix_a, matrix_b)

def user_matrices():
    """
    Prompt the user to input two 3x3 matrices and validate input
    """
    print('\nEnter integers for Matrix A and Matrix B.')
    print('Integers must be spaced apart (ex: # # #).')
    print('\nMatrix A: ')
    row1 = get_row(1)
    row2 = get_row(2)
    row3 = get_row(3)
    matrix_a = np.array([row1, row2, row3], dtype=np.float64)
    print("Finalized Matrix (A):")
    print_format(matrix_a)

    print("\nMatrix B: ")
    row1 = get_row(1)
    row2 = get_row(2)
    row3 = get_row(3)
    matrix_b = np.array([row1, row2, row3], dtype=np.float64)
    print("Finalized Matrix (B):")
    print_format(matrix_b)
    return matrix_a, matrix_b

def matrices_addition(a, b):
    """
    Function for addition operation
    """
    added = a + b
    return added

def matrices_subtraction(a, b):
    """
    Function for subtraction operation
    """
    subtracted = a - b
    return subtracted

def matrices_multiplication(a, b):
    """
    Function for multiplication operation
    """
    multiplied = np.matmul(a, b)
    return multiplied

def transpose(a, b):
    """
    Function for tranpose operation
    """
    transpose_a = np.transpose(a)
    transpose_b = np.transpose(b)
    return transpose_a, transpose_b

def exit_program():
    """
    Immediately exits the program
    """
    print('Thanks for playing!')
    print('Exiting the game...')
    return False

def matrices_menu(matrix_a, matrix_b):
    """
    Menu for Matrix Operations
    1. Addition
    2. Subtraction
    3. Matrix Multiplication
    4. Matrix Transposition
    """
    user_choice = True
    while user_choice:  # Menu Loop
        print("\n      Matrix Operation Operations: ")
        print('1. Addition')
        print('2. Subtraction')
        print('3. Matrix Multiplication')
        print('4. Transpose')
        print('5. Exit program')
        selection = input('\n      Enter your choice: ')

        if selection == '1':
            result = matrices_addition(matrix_a, matrix_b)
            print('\nMatrix Addition Result: ')
            print_format(result)
        elif selection == '2':
            result = matrices_subtraction(matrix_a, matrix_b)
            print('\nMatrix Subtraction Result: ')
            print_format(result)
        elif selection == '3':
            result = matrices_multiplication(matrix_a, matrix_b)
            print('\nMatrix Multiplication Result: ')
            print_format(result)
        elif selection == '4':
            transpose_a, transpose_b = transpose(matrix_a, matrix_b)
            print('\nTransposed Matrices: ')
            print('Matrix A: ')
            print_format(transpose_a)
            print('Matrix B: ')
            print_format(transpose_b)
        elif selection == '5':
            user_choice = exit_program()
        else:
            print('Error. Invalid selection.')

def main():
    """ Main Program Entry Point """
    print('     Do you want to play the matrix game?')
    print('     Answer the following prompt to begin.')
    user_prompts()

main()

# Created by Alexis Krueger, CYOP 300, Sep. 12 2024
