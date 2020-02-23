# fruits = ["mango", "grapes", "guava", "apple"]
# for fruits in fruits:
#   print("current fruits", fruits)

# print("goodbye")

'''
num = int(input("Number: "))
factorial = 1
if num < 0:
    print("must be positive")
elif num == 0:
    print("factorial + 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
print(factorial)
'''
'''
print("Welcome to Guaranty trust bank ATM")
restart = "Y"
chances = 3
balance = 200000
while chances >= 0:
    pin = int(input("please enter your 4 digit pin"))
    if pin == (1983):
        print("you entered your pin correctly\n")
        while restart not in ("n", "NO", "no", "N"):
            print("please press 1 for your balance\n")
            print("please press 2 to make a withdrawal\n")
            print("please press 3 to pay in\n")
            print("please press 4 to Return card\n")
            option = int(input("what would you like to choose?"))
            if option == 1:
                print("your balance is #, balance,\n")
                restart = input("would you like to go back? ")
                if restart in ("n", "NO", "no", "N"):
                    print("thank you")
                    break
            elif option == 2:
                option2 = ("Y")
                withdrawal = float(
                    input("how much would you like to withdraw? \n#200/#500/#700/#1000"))
                if withdrawal in [200, 500, 700, 1000]:
                    balance = balance - withdrawal
                    print("\nyour balance is now #", balance)
                    restart = input("would you like to go back? ")
                    if restart in ("n", "NO", "no", "N"):
                        print("thank you")
                        break
                elif withdrawal != [200, 500, 700, 1000]:
                    print("invalid amount, please retry\n")
                    restart = ("Y")
                elif withdrawal == 1:
                    withdrawal = float(
                        input("please enter a desired amount: "))

            elif option == 3:
                pay_in = float(input("how much would you like to pay in? "))
                balance = balance + pay_in
                print("\nYour balance is now #, balance")
                restart = input("would you like to go back? ")
                if restart in ("n", "NO", "no", "n"):
                    print("thank you")
                    break
                elif option == 4:
                    print("please wait whilst your card is returned...\n")
                    print("thank you for your patronage")
                    break
                else:
                    print("please enter a correct number. \n")
                    restart = ("Y")
    elif pin != ("1983"):
        print('incorrect password')
        chances = chances - 1
        if chances == 0:
            print("\nNo more tries")
            break
'''

'''
secret_number = 10
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("guess: "))
    guess_count += 1
    if guess == secret_number:
        print("you win!")
        break
else:
    print("sorry you failed!")
'''

'''
command = ""  # empty string which has no character only qoutes.
started = False
while True:
    command = input("give your command: ").lower()
    if command == "start":
        if started:
            print("car is already started!")
        else:
            started = True
            print("car started.......")
    elif command == "stop":
        if not started:
            print("car is already stopped!")

        else:
            started = False
            print("car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit        
        """)
    elif command == "quit":
        break
    else:
        print("sorry i dont understand that")
'''


# for loops
'''
prices = [200, 300, 100]
total = 0
for price in prices:
    total += price  # total = total + price
print(f"the price total is: {total}")
'''

# for x in range(4):  # nested loops
# for y in range(3):
#print(f"({x}, {y})")

'''
numbers = [10, 4, 10, 4, 4, 4]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output = output + "x"
    print(output)

# you can also code like this:

numbers = [10, 4, 10, 4, 4, 4, 4]
for x_count in numbers:
    print("x" * x_count)
'''



