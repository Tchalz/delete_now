'''
x = input("x: ")
y = int(x) + 1
print(f"x:{x}, y:{y}")
'''

'''
temperature = 50
if temperature > 110:
    print("Jesus is the king of kings")
    print("Jesus said, 'i saw satan fall like lightening' ")
elif temperature > 100:
    print("it is a great thing to serve Jesus")
else:
    print("it is finished!")
'''
# ternary operator
# age = 40
# message = "eligible" if age >= 30 else "not eligible"
# print(message)


# logical operator:and,or,not

'''
high_income = True
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("eligible")
else:
    print("not eligible")
'''

# chaining comparison operators
# age = 22
# if age >= 18 and age <65:
#   print("Eligible")
'''
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
'''

# loops: we use loops to create repetitions

# for
# for number in range(1, 20, 2):
# print("JESUS IS THE SWEETEST NAME I KNOW", number, number * ".")


# for else
'''
successful = False
for number in range(5):
    print("attempted")
    if successful:
        print("successful")
        break  # to jump out of the loop

else:
    print("attempted 5 times and failed")
'''

# nested loops
# for x in range(5):
#   for y in range(4):
#      print(f"({x}, {y})")

'''
reasons why python is the most popular programming language cos:
1: with python youn can solve complex problems with with fewer lines of code than many other languages
 # str.substring(0, 3), javascript str.subtr(0, 3), but python str[0, 3]
 eg. to extract he in hello world...c
2 python is a multipurpose language for a wide range of jobs like: data analysis, AI/ML, automation, web apps, mobile apps, desktop apps, software testing and even hacking.
3: python is a high level language so dont worry about complex tasks like memory management(large ones and data)
4:cross-platform: it can be implemented using windows, linux, mac
5: huge community: whenever you are stucked programming there is always someone out there to help
6: large ecosystem: of libraries, frame works and tools
'''

'''
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
'''

'''
# iterables:
for x in "python":   #for loops are used to iterate iterable objects.
    print(x)

for x in [1, 2, 3, 4, 5]:
    print(x)
'''

# while loops: are used to repeat something especially if their condition is true.
'''
number = 100
while number > 0:      # we want to evaluate a condition while repeating a task
    print(number)       # number = number // 2(the same),
    number = number // 2
'''

# infinite loops: is a loop that runs forever....

# exercise
'''
count = 0                     revisit this exercise again
for number in range(1, 10):
    if number % 2 == 0:
        count = count + 1  # count += 1
        print(number)
print(f"we have {count} even number")
'''


# functions: A function is a block of organized, reusable code that is used to perform a single, related action
# As you already know, Python gives you many built-in functions like print(), etc. but you can also create your own functions.
# parameter: the input that you define for your function
# Argument: is the actual value for a given parameter
'''
def greet(first_name, last_name):  #parameter (function that performs a task)
    print(f"hi {first_name} {last_name}")
    print("welcome aboard")


greet("charles", "emmanuella")   #arguments
greet("chinyere", "jonathan")
greet("ijeoma", "okpara")
'''

# types of functions:
# 1:functions that perform a task
# 2:functions that calculate and return a value e.g round(1.9)

'''
def get_greeting(first_name, last_name, object):
    # print(f"Hi {name}")
                          # this particular function just prints to a terminal
    return f"hi {first_name} {last_name} i would like you to get the {object} for me"


silk = print(get_greeting("chibuzor", "nwozuzu", "flat television"))


# in python all functions by default returns "none" value(none is an object that represents the absence of a value )




def get_greeting(name):
    return f"hi {name}"
                           # this particular function not only prints to a terminal, but can also be re-usable
                           # in the future, ie write it in a file or send it an email.

message = get_greeting("mosh")
print(message)
# KEYWORD ARGUMENt
# def increment(number, by):
# return number + by


# print(increment(20, by=1000))


# DEFAULT ARGUMENT              #by=30 is now a default argument
# def increment(number, by=30):  # by=30 is now made optional ie we can also add a second argument to our print function and it will be be executed
# return number + by


# print(increment(90))

'''
# args, wait, what?
def multiply(*numbers):
    x = 1
    for number in numbers:
        x *= number
    return x
    


print(multiply(3, 4, 2, 7))
'''

'''
# **args(for dictionaries)
def save_user(**user):  # keyword argument: name=chibuzor
    # or user[name] or user[age]    #print either of these arguments
    print(user["age"])


save_user(id=1, name="john", age=22)
'''


# SCOPE     region of the code where a variable is defined
def greet():  # the scope of the variable(message) is the greet()
    message = "a"


            