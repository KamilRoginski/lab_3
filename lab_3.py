#Name: Kamil Roginski
#Date: 26 MAR 2025
#Professor:Mark Babcock
#Course: CYOP 300

"""This program was created for Week 3 Lab3 assignment. I've created a command line
menu-driven python application providing users with the ability to search and display
U.S. State Capital, population and Flowers.

This program includes the following options:
1. Display all U.S. States in Alphabetical order along with the Capital, State Population,
and Flower

2. Search for a specific state and display the appropriate Capital name, State Population,
and an image of the associated State Flower.

3. Provide a Bar graph of the top 5 populated States showing their overall population.

4. Update the overall state population for a specific state.

5. Exit the program
"""

import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Sample data for U.S. states. Each state f represented as a dictionary containing:
# 'name', 'capital', 'population', 'flower', and 'image' (the filename for the flower image).
states_data = [
    {
        "name": "Alabama",
        "capital": "Montgomery",
        "population": 4903185,
        "flower": "Camellia",
        "image": "alabama_flower.jpg"
    },
    {
        "name": "Alaska",
        "capital": "Juneau",
        "population": 731545,
        "flower": "Forget-me-not",
        "image": "alaska_flower.jpg"
    },
    {
        "name": "Arizona",
        "capital": "Phoenix",
        "population": 7278717,
        "flower": "Saguaro Cactus Blossom",
        "image": "arizona_flower.jpg"
    },
    {
        "name": "Arkansas",
        "capital": "Little Rock",
        "population": 3017804,
        "flower": "Apple Blossom",
        "image": "arkansas_flower.jpg"
    },
    {
        "name": "California",
        "capital": "Sacramento",
        "population": 39512223,
        "flower": "California Poppy",
        "image": "california_flower.jpg"
    }
]

def display_states(states):
    """
    Display all U.S. states in alphabetical order along with their capital, population, and flower.
    """
    sorted_states = sorted(states, key=lambda x: x["name"])
    print("\nAll U.S. States (Alphabetical Order):")
    print(f"{'state':<15} {'Capital':<15} {'Population':<15} {'Flower':<25}")
    print("-" * 70)
    for state in sorted_states:
        print(f"{state['name']:<15} {state['capital']:<15} {state['population']:<15} {state['flower']:<25}")
    print()  # blank line for readability

def search_state(states):
    """
    Search for a specific state and display its capital, population, and state flower image.
    """
    state_name = input("Enter the state name to search: ").strip()
    found = False
    for state in states:
        if state["name"].lower() == state_name.lower():
            found = True
            print("\nState Found!")
            print(f"State: {state['name']}")
            print(f"Capital: {state['capital']}")
            print(f"Population: {state['population']}")
            print(f"Flower: {state['flower']}")
            # Attempt to display the state flower image if the file exists
            image_path = state["image"]
            if os.path.exists(image_path):
                try:
                    img = mpimg.imread(image_path)
                    plt.imshow(img)
                    plt.axis('off')
                    plt.title(f"{state['name']} State Flower: {state['flower']}")
                    plt.show()
                except (OSError, ValueError) as e:
                    print(f"Error displaying image: {e}")
            else:
                print(f"Image file '{image_path}' not found.")
            break
    if not found:
        print("State not found. Please try again.\n")

def show_bar_graph(states):
    """
    Provide a bar graph of the top 5 populated states.
    """
    # Sort states by population in descending order and select the top 5
    top_states = sorted(states, key=lambda x: x["population"], reverse=True)[:5]
    state_names = [state["name"] for state in top_states]
    populations = [state["population"] for state in top_states]

    plt.figure()
    plt.bar(state_names, populations)
    plt.xlabel("States")
    plt.ylabel("Population")
    plt.title("Top 5 Populated States")
    plt.show()

def update_population(states):
    """
    Update the overall state population for a specific state.
    """
    state_name = input("Enter the state name to update population: ").strip()
    for state in states:
        if state["name"].lower() == state_name.lower():
            print(f"Current population for {state['name']}: {state['population']}")
            while True:
                try:
                    new_population = int(input("Enter the new population: ").strip())
                    if new_population < 0:
                        print("Population cannot be negative. Please try again.")
                        continue
                    state["population"] = new_population
                    print(f"Population updated successfully for {state['name']}.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer value for population.")
            return
    print("State not found. Please try again.\n")

def main():
    """
    Main function to run the command line menu-driven application.
    The program loops until the user selects the exit option.
    """
    while True:
        print("====================================")
        print("Welcome to the U.S. State Info Application!")
        print("Please choose an option:")
        print("1. Display all U.S. States")
        print("2. Search for a specific state")
        print("3. Show bar graph of top 5 populated states")
        print("4. Update state population")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_states(states_data)
        elif choice == "2":
            search_state(states_data)
        elif choice == "3":
            show_bar_graph(states_data)
        elif choice == "4":
            update_population(states_data)
        elif choice == "5":
            print("Thank you for using the U.S. State Info Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
