#EXERCISE ONE: GUESSING GAME!
'''
secret_number = 100
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    guess = int(input("guess: "))
    guess_count += 1
    if guess == secret_number:
        print("you won! ")
        break
else:
    print("you lose!!!")
'''

#EXERCISE TWO: PROGRAM FOR CONTROLLING A CAR
'''
command = ""
started = False
while True:
    command = input("=").lower()
    if command == "start":
        if started:
            print("car is already started! ")
        else:
            started = True
            print("car started.....ready to go! ")
    elif command == "stop":
        if not started:
            print("car is already stopped! ")
        else:
            started = False
            print("car stopped. ")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
              """)
    elif command == "quit":
        break
    else:
        print("sorry i dont understand the command")
'''