#   FILE:   ui_helper.py
#   DATE:   2021-10-11
#   AUTHOR: loulou Muluile
#   DESCRIPTION:
"""
These are utility function for interacting with the user on the command line.
if done correctly, these can be used by multiple program.

"""
import mathQuiz
#########################################################################################
# Functions for general user interaction
#########################################################################################

def show_message(message):
    """
    Display a message in a standard format.

    INPUTS:
        message string The message to display

    """
    print(message)
def show_program_title(title, width):
    """
    displays the program title in a standard manner.

    INPUTS:
        title A string with the title of the program.
        width An int with the screen width for display, in characters.
    """
    new_title = '***' + title.upper() + ' ***'
    print(f'\n{new_title:^{width}}')


def show_section_title(title):
    """
    displays a section title in a consistent format.

    INPUTS:
        title A string  with the section title text.
    """
    print(f'\n\t--{title}--')

def press_enter_key_to_continue():
    """
    Tells the user to hit the Enter key to continue. Waits until they do.
    Any other is ignored.
    """
    input('\nPress the Enter ket to continue..')



#########################################################################################
# Functions for menus
#########################################################################################

def get_user_choice():
    """
    Displays a menu, asks the user for a choice, and returns the choice as a
    string.

    Returns:
        string A string representing the user's choice

    """
    menu_title = "Main Menu"
    prompt ="Your choice: "  # remember the space at the end of the prompt
    options = ['1) Add an Employee', '2) Show All Employees'
        , '3) View an Employee', '4) Update an Employee'
        , '5) Delete an Employee', 'Q) Quit']
    show_menu(menu_title,options)
    # Return the user's choice
    return input(prompt)

def show_menu(title, options):
    """
    Displays a menu in structured manner.

    INPUTS:
        title A string with the file of the menu
        options A list of strings containing options to displays

    """
    print(f'\n\n\t-- {title} --')
    for option in options:
        print(f'\t{option}')

def confirm_quit():
    """
    Displays a message starting that the user has chose to quit and asks them
    to confirm. if they enter 'Y' or 'y', then this function returns True,
    otherwise returns False.

    Returns:
        Boolean True if confirmed , False otherwise
    """
    show_message("\nYou chose to quit the program.")
    choice = input("Confirm quit (Y/N) ")
    return choice == 'Y' or choice == 'y'

