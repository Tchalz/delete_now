import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:  # while loop: the number of iterations not known unlike for loop
    guess = int(input("new number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("number too large")
        elif guess < to_be_guessed:
            print("number too small")
        else:
            print("sorry that you are giving up!")
            break
else:
    print("congratulation, you made it!")
