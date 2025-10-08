#C Major's Calculator
import math
import random

#History storage
history = []

#Introductory message
print("Hello! Welcome to C Major's Calculator!")

#General calculator function
def calculator():    
    menu = ["Addition", "Subtraction", "Division", "Multiplication", "Multiplication Table", "Square", "Square Root", "Games", "History", "Exit"]

    print('-' * 20)

    for i, menu in enumerate(menu,start=1):
        print(f"{i}. {menu}")

    while True:
        print("-" * 20)
        request = input("Select an option from the menu: ").lower()

#Addition
        print('-' * 20)
        if request == "addition" or request == "1":
            try:
                num1 = float(input("Input your first number: "))
                num2 = float(input("Input your second number: "))
                result = num1 + num2
                print(result)
                history.append(f"{num1} + {num2} = {result}")
                offline_history()
                print('-' * 20)
            except:
                print("Error! Cross-check your inputs!")
                print('-' * 20)

#Subtraction
        elif (request == "subtraction" or request == "2"):
            try:
                num1 = float(input("Input your first number: "))
                num2 = float(input("Input your second number: "))
                result = num1 - num2
                print(result)
                history.append(f"{num1} - {num2} = {result}")
                offline_history()
                print('-' * 20)
            except:
                print("Error! Cross-check your inputs!")
                print('-' * 20)

#Division
        elif (request == "division" or request == "3"):
            try:
                num1 = float(input("Input your first number: "))
                num2 = float(input("Input your second number: "))
                if num2 == 0:
                    print("Error! Numbers cannot be divisible by 0!")
                else:
                    result = num1 / num2
                    print(result)
                    history.append(f"{num1} / {num2} = {result}")
                    offline_history()
                    print('-' * 20)
            except:
                print("Error! Cross-check your inputs!")
                print('-' * 20)

#Multiplication
        elif request == "multiplication" or request == "4":
            try:
                num1 = float(input("Input your first number: "))
                num2 = float(input("Input your second number: "))
                result = num1 * num2
                print(result)
                history.append(f"{num1} * {num2} = {result}")
                offline_history()
                print('-' * 20)
            except:
                print("Error! Cross-check your inputs!")
                print('-' * 20)

#Multiplication table
        elif request == "multiplication table" or request == "5":
            multiplication_table()
            print('-' * 20)

#Square
        elif request == "square" or request == "6":
            try:
                num = float(input("Input the number you would like to square: "))
                num_square = float(input("Input the number you would like to square your initial number by: "))
                result = num ** num_square
                print(result)
                history.append(f"{num} ** {num_square} = {result}")
                offline_history()
                print('-' * 20)
            except:
                print("Error! Cross-check your inputs!")
                print('-' * 20)

#Square root
        elif request == "square root" or request == "7":
            try:
                root_number = float(input("Input the number you would like to find it's square root: "))
                root = math.sqrt(root_number)
                print(root)
                history.append(f"The root of {root_number} is {root}")
                offline_history()
                print('-' * 20)
            except:
                print("Error! Cross-check your inputs!")
                print('-' * 20)

#Games
        elif request == "games" or request == "8":
            try:
                game_menu = ["Guess The Number"]
                for i, game_menu in enumerate(game_menu,start=1):
                    print(f"{i}. {game_menu}")

                choose = input("Pick an option from the above: ").lower()
        #Guess the game
                if choose == "guess the game" or choose == "1":
                    random_number()
                    print('-' * 20)
                elif choose != "guess the game" or choose != "1":
                    print("Other games to be released soon!")
                    calculator()
            except:
                print("Error! Cross-check your inputs!")
                print('-' * 20)

#History
        elif request == "history" or request == "9":
            try:
                history_menu = ["Show History","Clear History"] 
                for i, history_menu in enumerate(history_menu,start=1):
                        print(f"{i}. {history_menu}")

                select = input("Pick an option from the above: ").lower()
        #show history
                if select == "show history" or select == "1":
                    print("Preparing history...")
                    if not history:
                        print("No history yet!")
                    else:
                        for i, item in enumerate(history,start=1):
                            print(f"{i}. {item}")
                            print("-" * 20)
        #clear history
                elif select == "clear history" or select == "2":
                    print('-' * 20)
                    history.clear()
                    print("History cleared!")
                    print('-' * 20)
            except:
                print("Error! Cross-check your inputs!")
                print('-' * 20)
            
#Exit
        elif request == "exit" or request == "10":
            exit = input("Are you sure you want to leave the calculator? (Yes/No): ").lower()

            if (exit == "yes"):
                print('-' * 20)
                print("Goodbye!")
                return

            elif exit == "no":
                calculator()

            else:
                print('-' * 20)
                print("Invalid! Must input a 'Yes' or a 'No'!")
                calculator()
            break

#If inputs don't match      
        else:
            print("Invalid! Cross-check your input(s)!")
            print('-' * 20)


#Multiplication table function
def multiplication_table():
    try:

        multi_table = str(input("Would you like a multiplication table? (Yes/No): ")).lower()

        if multi_table == "yes":
            table_number = int(input("Input the number you would like to generate it's multiplication table: "))
            table_lines = []

            for i in range(1, 13):
                line = (f"{table_number} * {i} = {table_number * i}")
                print(line)
                table_lines.append(line)
                table_entry = (f"Multiplication Table of {table_number}:\n" + "\n".join(table_lines))   
            history.append(table_entry)
            offline_history()

        elif multi_table == "no":
            return    

        elif multi_table != "yes" or multi_table != "no":
            print("Error! Please input a 'Yes' or a 'No'!")
    except:
        print("Error! Cross-check your inputs!")
        print('-' * 20)
        multiplication_table()


#Writing history to a file
def offline_history():
    with open('offlineHistory.txt', 'w') as file:
        file.write("C Major's Calculator\n")
        file.write("Offline history:\n")
        file.write('-' * 20 + '\n')
        for result in history:
            for i, result in enumerate(history,start=1):
                file.write(f"{i}. {result}" + '\n')
                file.write('-' * 20 + '\n')
            break


#Random number/Guess The Game function
def random_number():
    try:
        secret_num = random.randint(1,20)
        print('-' * 20)
        print("I have a secret number ranging from 1 - 20")
        print("Guess the number...")
        for i in range(1,5):
            guess_num = int(input("What do you think the secret number is?: "))
            if guess_num > secret_num:
                print("Your guessed number is above the secret number.")
            elif guess_num < secret_num:
                print("Your guessed number is below the secret number.")
            elif guess_num > 20:
                print("Invalid! Guess numbers from 1 - 20 only!")
            elif guess_num < 1:
                print("Invalid! Guess numbers from 1 - 20 only!")
            else:
                 break
             
        if guess_num == secret_num:
            print("Congratulations! You guessed the secret number correctly!")
        else:
            print("Your guess is wrong. The secret number is", secret_num)

        replay = input("Would you like to play again? (Yes/No): ").lower()
        if replay == "yes":
            random_number()
        elif replay == "no":
            calculator()
        else:
            print("Invalid! Please input a 'Yes' or a 'No'!")
    except:
        print("Error! Cross-check your inputs!")
        print('-' * 20)


#Calling the general function    
calculator()