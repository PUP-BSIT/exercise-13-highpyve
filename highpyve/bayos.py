import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def buffer():
   input("Press Enter to return to menu...")
   clear_screen()

def bayos_main():
   clear_screen()

   while True:
       print("*************************************************")
       print("     Good Day! My name is Eurielle T. Bayos.")
       print("*************************************************")
       print("1. Eurielle’s Basic Information.")
       print("2. Eurielle’s Goals in life.")
       print("3. Jaira's Comment")
       print("4. Mikaela's Comment")
       print("0. Exit.")
       print("*************************************************")
       try:
           user_input = int(input("Enter your choice from 1-4: "))
       except ValueError:
           print("Invalid input. Please try again.")
           buffer()
           continue

       match user_input:
           case 1:
               show_basic_info()
           case 2:
               show_goals()
           case 3:
               print("\nRooting for you always, Eurielle. " \
               "You’re meant for great things.")
               buffer()
           case 4: 
                print("Comment from Highpyve-Mika")
                print("Hope you live a better life from now on!\n")
           case 0:
               print("\nThank you for visiting Eurielle's profile!")
               break
           case _:
               print("Invalid input. Please enter a valid number.")
               buffer()

def show_basic_info():
   clear_screen()
   print("*************************************************")
   print("\t\tEurielle's Basic Information")
   print("*************************************************")
   print("Name: Eurielle T. Bayos")
   print("Birthdate: August 27, 2003")
   print("Age: 21 Years Old")
   print("Sex: Male")
   print("Address: Barangay Katuparan, Taguig City")
   print("College: PUP - Taguig")
   print("Program: Bachelor of Science in Information Technology")
   print("*************************************************")
   buffer()

def show_goals():
   clear_screen()
   print("*************************************************")
   print("\t\tEurielle's Goals")
   print("*************************************************")
   print("1. To become successful in life.")
   print("2. To live a life where I can do the things I love.")
   print("3. To continuously learn and grow.")
   print("4. To live a better life.")
   print("*************************************************")
   buffer()
