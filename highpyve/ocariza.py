import os
from colorama import Fore, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def buffer():
    input("\nPress [ENTER] to return to main menu...")
    clear_screen()

def ocariza_menu():
    clear_screen()

    while True:
        print(Fore.LIGHTMAGENTA_EX 
              + "\n=== Welcome to Jaira Isabel Ocariza's Menu ===")
        print("1. Basic Information")
        print("2. Goals")
        print("3. Fun Facts")
        print("4. Mikaela's Comment")
        print("5. Kristoffer's Comment")
        print("6. Eurielle's Comment")
        print("7. Rose's Comment")
        print("0. Exit")

        try:
            choice = int(input(Fore.LIGHTYELLOW_EX + "\nEnter your choice: "))
        except ValueError:
            print(Fore.LIGHTRED_EX + "Please enter a valid number.")
            continue

        match choice:
            case 1:
                show_basic_info()
            case 2:
                show_goals()
            case 3:
                show_fun_facts()
            case 4:
                print("Comment from Highpyve-Mika")
                print("Drop skincare routine!\n")
            case 5: 
                print("You’ve done a solid and thorough job!")
                buffer()
            case 6:
                print("I really appreciate  your reliability, " \
                "you're someone we can always count on.")
                buffer()
            case 6:
                print("Comment from Highpyve-Rose")
                print("Amazing work, Jaira! Your colorful, well-crafted"
                      "interface makes your code both fun and impressive")
                buffer() 
            case 0:
                print(Fore.LIGHTYELLOW_EX + "Exiting menu... Goodbye!")
                break
            case _:
                print(Fore.LIGHTRED_EX + "Invalid choice. Please try again.")

def show_basic_info():
    clear_screen()
    print(Fore.LIGHTMAGENTA_EX + "Basic Information")
    print("Name: Jaira Isabel F. Ocariza")
    print("Age: 19")
    print("Gender: Female")
    print("Birthday: October 2, 2005")
    print("Status: Student at PUP Taguig - BSIT 2-1")
    buffer()

def show_goals():
    clear_screen()
    print(Fore.LIGHTMAGENTA_EX + "Goals")
    print("- I aspire to become a skilled Full Stack Developer,")
    print("- who crafts intuitive and elegant digital experiences!")
    buffer()

def show_fun_facts():
    clear_screen()
    print(Fore.LIGHTMAGENTA_EX + "Fun Facts")
    print("- I enjoy skincare routines as self-care.")
    print("- Patch, my dog, is my coding buddy!")
    print("- I secretly enjoy debugging—it's like solving a mystery.")
    buffer()

