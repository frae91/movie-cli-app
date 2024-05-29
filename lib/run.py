from env import session, clear
from models import Movie, Actor, Genre, MovieGenre, Cast, User, Fave

logged_user = None

def heading(text):
    print("*"*30)
    print(text)
    print("*"*30)

def handle_yes_no(message):
    returned_val = True
    while True:
        print(message)
        choice = input()

        if choice.lower() == "yes" or choice.lower() == "y":
            returned_val = True
            break
        elif choice.lower() == "no" or choice.lower() == "n":
            returned_val = False
            clear()
            break
        else:
            print(Fore.RED + "Invalid input" + Style.RESET_ALL)
    return returned_val

def main_menu():
    heading("MAIN MENU")

    print("all   - display all movies")
    print("genre - search movies by genre")
    print("actor - search movies by actor")
    print('faves - display all faves')
    print('exit  - terminate the program')

    print("\nPlease enter you menu choice:")
    return input()

def greet():
    pass

def start():
    greet()
    loop = True
    while loop:
        choice = main_menu()
        while True:
            if choice.lower() == 'all':
                break
            elif choice.lower() == 'genre':
                break
            elif choice.lower() == 'actor':
                break
            elif choice.lower() == 'faves':
                break
            elif choice.lower() == 'exit' or choice.lower() == 'quit':
                loop = False
                break
            else:
                print("Invalid input. Please try again!")

    print("Thank you for using the Movies DB App. Goodbye!")

if __name__ == "__main__":
    start()