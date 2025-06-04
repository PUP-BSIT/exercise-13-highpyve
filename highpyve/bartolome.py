import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def buffer():
    input("\nPress [ENTER] to return to main menu...")
    clear_screen()

def bartolome_menu():
    while True:
        clear_screen()
        print("*************************************************")
        print("    Hi! My name is Mikaela Joy T. Bartolome.")
        print("*************************************************")
        print("1. Know my Basic Information.")
        print("2. Know my Goals in life.")
        print("3. Know my favorite things.")
        print("4. Jaira's Comment")
        print("5. Kristoffer's Comment")
        print("6. Eurielle's Comment")
        print("7. Rose's Comment")
        print("0. Exit profile.")
        print("*************************************************")
        
        try:
            user_input = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            buffer()
            continue

        match user_input:
            case 1:
                show_basic_info()
            case 2:
                show_goals()
            case 3:
                show_favorites()
            case 4:
                clear_screen()
                print("Your dreams are valid, and your direction is clear." 
                      "Keep going, Mika!")
                buffer()
            case 5: 
                clear_screen()
                print("You did a really great job!")
                buffer()
            case 6:
                clear_screen()
                print("Your attention to detail is impressive, Bartolome.")
                buffer()
            case 7:
                show_tolentino_comment() 
            case 0:
                print("Thank you for visiting Mikaela's profile!")
                break
            case _:
                print("Invalid input. Please try again.")
                buffer()

def show_basic_info():
    clear_screen()
    print("*************************************************")
    print("\t  Mikaela's Basic Information")
    print("*************************************************")
    print("Nickname: Mika")
    print("Age: 19 Years Old")
    print("Sex: Female")
    print("Birthdate: November 24, 2004")
    print("Address: Lower Bicutan, Taguig City")
    print("Program: BS in Information Technology")
    print("School: PUP - Taguig")
    print("*************************************************")
    buffer()

def show_goals():
    clear_screen()
    print("*************************************************")
    print("\t\tMikaela's Goals")
    print("*************************************************")
    print("1. To read a lot of books or novels")
    print("2. To travel abroad")
    print("3. To attend a concert of my favorite artist")
    print("4. To be a successful professional.")
    print("*************************************************")
    buffer()


def show_favorites():
    clear_screen()
    print("*************************************************")
    print("\t    Mikaela's Favorite Things")
    print("*************************************************")
    print("1. Books, specifically with Fantasy genre.")
    print("2. Music, whatever genre.")
    print("3. My Melody merch or anything pink.")
    print("4. Karaoke booths.")
    print("*************************************************")
    buffer()

def show_tolentino_comment():
    clear_screen()
    print("Comment from Highpyve-Rose")
    print("Nice work, Mika! Your organized and lively code reflects"
            " great enthusiasm!")
    buffer()