import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def buffer():
    input("Press [ENTER] to return to main menu...")
    clear_screen() 

def anipan_menu(): 
    clear_screen()
    
    while True: 
        print("Hello! My name is Sigmund Kristoffer S. Anipan.")
        print("\nPlease choose an option:")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Jaira's Comment")
        print("4. Mikaela's Comment")
        print("5. Eurielle's Comment")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("\nInvalid input. Please try again.")
            continue

        match choice:
            case 1:
                show_basic_info()
            case 2:
                show_goals()
            case 3:
                print("\nClear code, clear goals. " \
                      "Keep coding with purpose, Kristoffer!")
                buffer()
            case 4:
                print("Comment from Highpyve-Mika")
                print("Hope you achieve every goal that you have!\n")
            case 5:
                print("Comment from Highpyve-Eurielle")
                print("Your ideas are always thoughtful and well-articulated.")
                buffer() 
            case 0:
                print("\nGoodbye! Thank you for visiting.")
                break
            case _:
                print("\nInvalid choice. Please enter a valid number.")

def show_basic_info():
    clear_screen()
    print("Basic Information")  
    print("\n1. Name: Sigmund Kristoffer S. Anipan")
    print("2. Age: 20 years old")
    print("3. Address: Ibayo-Tipas, Taguig City")
    print("4. Email: sigmund.anipan@example.com")
    print("5. Phone Number: 09XX-XXX-XXXX") 
    buffer()

def show_goals():
    clear_screen()
    print("Goals")
    print("\n1. To be successful in the future.")
    print("2. Learn a lot of paying skills.")
    print("3. Develop a strong and positive mindset.")
    print("4. Build healthy relationships with others.")
    print("5. Maintain a good balance between career and personal life.")
    print("6. Keep improving and learning continuously.")
    print("7. Make a positive impact on others and the community.")
    buffer()