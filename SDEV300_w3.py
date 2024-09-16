"""
This is a menu-driven program created to display U.S. State Info
Requirements:
-U.S. State capitals in alphabetical order followed by capital, population, and state flower
-Allow user to search for specific state and:
    display its capital, population, and an image of state flower
-Allow user to update a state's population
-Provides a bar graph of top 5 populated states
-User can exit the program
"""
import csv
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def load_flower_image(state_name, image_folder='/Users/alexis/Desktop/state flower'):
    """
    Loading the file images into the program
    """
    image_path = os.path.join(image_folder, f'{state_name.lower()}.jpg')

    if os.path.isfile(image_path):
        # Load and display the image
        img = mpimg.imread(image_path)
        plt.imshow(img)
        plt.axis('off')  # Hide the axis
        plt.title(f'{state_name} State Flower')
        plt.show()
    else:
        print(f'Image for {state_name} not found.')

def state_list():
    """
    Turning CSV file into a dictionary for easier & direct access to the data.
    This allows other functions to access specific keys.
    """
    state_dictionary = {}
    with open('state_info.csv', mode='r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            state_dictionary[row['state']] = {  # Using the state name (header) as the key
                'capital': row['capital'],
                'population': int(row['population']),
                'flower': row['flower']
            }
    return state_dictionary

def specific_state_search(state_name, states_data):
    """
    Searches for specific state info in the dictionary and displays it.
    """
    state_info_search = states_data.get(state_name)
    if state_info_search:
        print(f"{state_name}  Capital: {state_info_search['capital']} "
              f"| Population: {state_info_search['population']} | "
              f"State Flower: {state_info_search['flower']}")
        load_flower_image(state_name)  # Load the flower image for the state
    else:
        print('State not found. Try again.')

def update_state_information(states_data):
    """
    Updates the population of a state in the dictionary.
    """
    population_update = input('Enter the state to update its population data: ').strip().title()

    if population_update in states_data:
        try:
            new_population = int(input(f'Enter the new population for {population_update}: '))
            states_data[population_update]['population'] = new_population
            print(f"\nThe population of {population_update} has been updated to {new_population}.")
        except ValueError:
            print('Invalid input. Please enter a valid number for the population.')
    else:
        print('State not found. Try again.')

def population_bar_graph(states_data):
    """
    Generates a bar graph of the top 5 most populated states.
    """
    sorted_states = sorted(states_data.items(), key=lambda x: x[1]['population'], reverse=True)[:5]
    states, populations = zip(*[(state, info['population']) for state, info in sorted_states])

    plt.bar(states, populations, color='blue')
    plt.xlabel('States')
    plt.ylabel('Population')
    plt.title('Top 5 Most Populated States')
    plt.show()

def exit_program():
    """
    Immediately exits the program
    """
    print('Thank you for using the State Info Python Program.')
    print('Exiting the program...')
    return False

def main_menu():
    """
    Main menu loop to display the main menu &
    regenerate it upon completion of a chosen function
    """
    state_data = state_list()  # Load state data once for menu use
    user_choice = True
    while user_choice:  # Menu Loop
        print('\n          The Menu')
        print('a. Generate list of U.S. States including the: '
              'capital, population, and state flower.')
        print('b. Search for specific state information.')
        print('c. Update state information.')
        print('d. Generate a bar graph of the top 5 populated states.')
        print('e. Exit program')
        selection = input('\n      Enter your choice: ')

        if selection == 'a':
            for state, info in state_data.items():
                print(f"{state}  Capital: {info['capital']} | "
                      f"Population: {info['population']} | State Flower: {info['flower']}")
        elif selection == 'b':
            state_info = input('Enter U.S. State: ').strip().title()
            specific_state_search(state_info, state_data)
        elif selection == 'c':
            update_state_information(state_data)
        elif selection == 'd':
            population_bar_graph(state_data)
        elif selection == 'e':
            user_choice = exit_program()
        else:
            print('Error. Invalid selection.')

def main():
    """
    Main entry point of the program.
    """
    print('Welcome to the U.S. State Info Python Program.')
    main_menu()

main()
