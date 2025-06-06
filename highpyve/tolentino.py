import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def buffer():
    input("\nPress [ENTER] to return to main menu...")
    clear_screen()
    
def tolentino_menu():
    clear_screen()
    
    while True:
        print("╔══════════════════════════════════════════════════════╗")
        print("║       Hi! Welcome to Ma. Rose L. Tolentino's Menu    ║")
        print("╠══════════════════════════════════════════════════════╣")
        print("║                                                      ║")
        print("║   [1] Basic Info                                     ║")
        print("║   [2] Motivational Quotes                            ║")
        print("║   [3] Jaira's Comment                                ║")
        print("║   [4] Mikaela's Comment                              ║")
        print("║   [5] Kristoffer's Comment                           ║")
        print("║   [6] Eurielle's Comment                             ║")
        print("║   [0] Return to Main Menu                            ║")
        print("║                                                      ║")
        print("╚══════════════════════════════════════════════════════╝")

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("\nInvalid input! Please enter a number.\n")
            buffer()
            continue

        match user_choice:
            case 1:
                show_basic_info()
            case 2:
                show_quotes()
            case 3:
                show_ocariza_comment()
            case 4:
                show_bartolome_comment()
            case 5:
                show_anipan_comment()
            case 6:
                show_bayos_comment()
            case 0:
                exit_program()
                break
            case _:
                print("\nInvalid input! Please try again.\n")
                buffer()
                
def show_basic_info():
    clear_screen()
    print("╔════════════════════════════════════╗")
    print("║           Basic Information        ║")
    print("╠════════════════════════════════════╣")
    print("║ Age    : 20 years old              ║")
    print("║ Gender : Female                    ║")
    print("║ School : PUP - Taguig              ║")
    print("╚════════════════════════════════════╝\n")
    buffer()

def show_quotes():
    clear_screen()
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                    Motivational Quotes                     ║")
    print("╠════════════════════════════════════════════════════════════╣")
    print("║ “Keep your face always toward the sunshine—and shadows     ║")
    print("║  will fall behind you.” – Walt Whitman                     ║")
    print("║                                                            ║")
    print("║ “The best preparation for tomorrow is doing your best      ║")
    print("║  today.” – H. Jackson Brown                                ║")
    print("║                                                            ║")
    print("║ “Opportunities don't happen, you create them.” –           ║")
    print("║  Chris Grosser                                             ║")
    print("╚════════════════════════════════════════════════════════════╝\n")
    buffer()

def show_ocariza_comment():
    clear_screen()
    print("Comment from Highpyve-Jaira")
    print("\nMotivated people motivate people— "
            "and you’re doing just that, Rose.")
    buffer()

def show_anipan_comment():
    clear_screen()
    print("Comment from Highpyve-Kristoffer")
    print("Keep up the good work, this turned out great!")
    buffer()

def show_bayos_comment():
    clear_screen()
    print("Comment from Highpyve-Eurielle")
    print("You handle challenges with such calm and focus.")
    buffer()

def show_bartolome_comment():
    clear_screen()
    print("Comment from Highpyve-Mika")
    print("We do create our opportunities. Love the quote!")
    buffer()

def exit_program():
    clear_screen()
    buffer()

