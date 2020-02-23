"""
def format_map(number):
    string = str(number)
    result = string.replace("234", "0")
    print(result)


format_map(+2348087685643)

"""


# x = "+23408078839849".replace("+234", "0")
# print(x)


'''
import random  # random helps us to generate non-step or scattered numbers


def sort_number(*args):
    numbers_list = args
    result_list = []
    for number in numbers_list:
        string = str(number)
        replaced = string.replace("+234", "0")
        result_list.append(replaced)

    print(result_list)


sort_number("+23468957594038", "+23480390488556",
            "+2345477857566586", "+234647889569674", "+23421092077448")


# for loop the number of times a block of code is executed is defined
# while loop has its number of iteration running until a condition is met(undefined)

for x in range(0, 50, 5):
    print(x)

import random
y = random.randint(0, 50,)
print(y)
'''


# FUNCTIONS
'''
def stickers(*args):                   #for taken in multiple arguments
    for item in args:
        print(item)


stickers("a", "b", "c", "d")
'''

'''
def chibuzor(number):  # for multiple number of argument we introduce *args to our function
    number = str(number)
    if "234" in number:
        y = number.replace("234", "0")
        print(y)


chibuzor(2348045637848)

'''

'''
def chibuzor(*args):  # for multiple number of argument we introduce *args to our function
    number_list = args
    result_list = []
    for number in number_list:
        string = str(number)
        replaced = string.replace("234", "0")
        result_list.append(replaced)
    print("This will be displayed on a \n New lIne")
    print(result_list)


chibuzor("234894656478364", "234567588593354673",
         "23483544667383", "234844536478498")

'''
#Algorithm is a step-by-step procedure, which defines a set of instructions to be executed in a certain order to get the desired output. Algorithms are generally created independent of underlying languages, i.e. an algorithm can be implemented in more than one programming language.

#From the datastructure point of view, following are some important categories of algorithms −

Search − Algorithm to search an item in a data structure.

Sort − Algorithm to sort items in a certain order.

Insert − Algorithm to insert item in a data structure.

Update − Algorithm to update an existing item in a data structure.

Delete − Algorithm to delete an existing item from a data structure.



Characteristics of an Algorithm
Not all procedures can be called an algorithm. An algorithm should have the following characteristics −

Unambiguous − Algorithm should be clear and unambiguous. Each of its steps (or phases), and their inputs/outputs should be clear and must lead to only one meaning.

Input − An algorithm should have 0 or more well-defined inputs.

Output − An algorithm should have 1 or more well-defined outputs, and should match the desired output.

Finiteness − Algorithms must terminate after a finite number of steps.

Feasibility − Should be feasible with the available resources.

Independent − An algorithm should have step-by-step directions, which should be independent of any programming code.

How to Write an Algorithm?
There are no well-defined standards for writing algorithms. Rather, it is problem and resource dependent. Algorithms are never written to support a particular programming code.

As we know that all programming languages share basic code constructs like loops (do, for, while), flow-control (if-else), etc. These common constructs can be used to write an algorithm.

We write algorithms in a step-by-step manner, but it is not always the case. Algorithm writing is a process and is executed after the problem domain is well-defined. That is, we should know the problem domain, for which we are designing a solution.

Example
Let's try to learn algorithm-writing by using an example.

Problem − Design an algorithm to add two numbers and display the result.

Step 1 − START
Step 2 − declare three integers a, b & c
Step 3 − define values of a & b
Step 4 − add values of a & b
Step 5 − store output of step 4 to c
Step 6 − print c
Step 7 − STOP
Algorithms tell the programmers how to code the program. Alternatively, the algorithm can be written as −

Step 1 − START ADD
Step 2 − get values of a & b
Step 3 − c ← a + b
Step 4 − display c
Step 5 − STOP
In design and analysis of algorithms, usually the second method is used to describe an algorithm. It makes it easy for the analyst to analyze the algorithm ignoring all unwanted definitions. He can observe what operations are being used and how the process is flowing.

Writing step numbers, is optional.

We design an algorithm to get a solution of a given problem. A problem can be solved in more than one ways.

one problem many solutions
'''


'''
#RETURN STATEMENT



def chibuzor(*args):  # for multiple number of argument we introduce *args to our function
    number_list = args
    result_list = []
    for number in number_list:
        string = str(number)
        replaced = string.replace("234", "0")
        result_list.append(replaced)
    return result_list


chibuzor("234894656478364", "234567588593354673",
         "23483544667383", "234844536478498")



#OOP(OBJECT ORIENTED PROGRAM)
# a class is not an object, but its deisgned from one.
# a class is a programming code that has the power to
please go and look at OOP and classes      #ASSIGNMENT