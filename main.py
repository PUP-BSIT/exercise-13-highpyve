import os
from highpyve import anipan, bartolome, tolentino, bayos, ocariza

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    print("==========================================")
    print("          Welcome to HighPyve!         ")
    print("==========================================")
    print("Select a developer module to continue:\n")
    print("[1] Kristoffer Anipan")
    print("[2] Ma. Rose Tolentino")
    print("[3] Mikaela Joy Bartolome")
    print("[4] Jaira Isabel Ocariza")
    print("[5] Eurielle Bayos")
    print("[0] Exit\n")
    
    try:
        user_choice = int(input("Enter your choice: "))
    except ValueError:
        print("\nInvalid input! Please enter a number.")
        input("Press Enter to continue...")
        continue
        
    match user_choice:
        case 1:  
            anipan.anipan_menu()
        case 2: 
            tolentino.tolentino_menu()
        case 3:  
            bartolome.bartolome_menu()
        case 4:  
            ocariza.ocariza_menu()
        case 5:  
            bayos.bayos_main()
        case 0:
            clear()
            print("Thank you for using HighPyve Main Menu! Exiting...")
            break
        case _:
            print("\nInvalid choice! Please select a number from 1 to 6.")
            input("\nPress Enter to continue...")