# print("\t hello world")
# print("python\nis awsome!")
# print(type(201))
# print(type(12.7))
# print(type(False))
# print(type(31))
# print(type("True"))
# print(True)
# x = 10
# y = "ten"
# temp = x
# x = y
# y = temp
# # y = x
# print(x)
# print(y)

# x = 10           #using a single line of code to swap the values of 2 variables
# y = "ten"
# y, x = x, y
# print(x)
# print(y)

# x = 12.5/2.5
# print(x)
# x = 5**2      #5 to the power 2
# print(x)

# x = float(input("please enter a number: "))
# print(x + 5)

# is_a_float = 1.655
# is_an_int = int(is_a_float)
# print(is_an_int)


# x = 1.5
# print(x)
# print(type(x))

# y = 3
# print(y)
# print(type(y))

# print(str(x))
# print(type(str(x)))
# print(str(y))
# print(type(str(y)))

# the_bool = bool(input("Please enter True or False: "))
# print(the_bool)
# print(type(the_bool))


# print(bool(0))
# print(bool(2))

# print(int(True))
# print(int(False))
# print(type(int(True)))

# cost = 200
# money = 400
# print(money > cost)
# print(type(money > cost))


# drink = input("What drink is available?")

# if drink == "soda":
#     print("I will purchase soda")

# elif drink == "juice":
#     print("I will purchase juice")
# else:
#     print("I will purchase water")


# temperature = int(input("please enter today's temperature: "))
# if temperature > 15:
#     print("it is cold")
# elif temperature < 15:
#     print("it is warm")
# else:
#     print("it is hot")




# is_water = input("Is water available (True or False)?")

# if is_water == "True":
#    print("i will get down to business")


# is_soda = True
# have_money = False

# if is_soda and have_money:
#     print("I will purchase this drink")
# else:
#     print("jesus is lord of all the universe!")


# is_soda = False
# have_money = False
# is_thirsty = False

# if is_soda and have_money and is_thirsty:
#     print("I will purchase this drink")
# else:
#     print("I will not purchase this drink")
#     if is_soda == False:
#         print("Soda is not available")
		
#     if have_money == False:
#         print("I do not have money")
		
#     if is_thirsty == False:
#         print("I am not thirsty")

# num = int(input("Please enter an integer value: "))

# if num > 0:
#     if num < 20:
#         print("The number is positive and less than 20")
#     else:
#         print("The number is positive")
# else:
#     print("The number is not positive")

# num = int(input("Please enter an integer value: "))

# if num > 0 and num < 20:
#     print("The number is positive and less than 20")

# elif num > 0:
#     print("The number is positive")

# else:
#     print("The number is not positive")



# fever = False
# cough = False
# fatigue = False

# if (fever or cough or fatigue):
#     print("I will see a doctor")
# else:
#     print("i will just flex and relax at home, watch movies and play some games!")

# password = "holiness4CHRIST@"     # Enter a value for password between the quotation marks before running the program

# if password != "8734":
#     print("Sorry, that's the wrong password")


# string = "JESUS CHRIST IS LORD!"
# print(string)
# new_string = string.capitalize()
# print(new_string)

# only_letters = "abcdef"
# print(only_letters.isalpha())    # True

# has_letters = "12mn3"
# print(has_letters.isalpha())     # False

# no_letters = "1245@"
# print(no_letters.isalpha())      # False

# import string
# only_symbols = "!@\#$^&\*"
# print(not only_symbols.isalnum())    # True

# no_symbols = "mnop123"
# print(not no_symbols.isalnum())     # False

# symbols_and_non_symbols = "mnop@123"
# print(not symbols_and_non_symbols.isalnum())     # True

# print(all(symbol in string.punctuation for symbol in only_symbols))     # True

# print(all(symbol in string.punctuation for symbol in no_symbols))     # False

# print(all(symbol in string.punctuation for symbol in symbols_and_non_symbols))     # False



# string = "1983chiboy"     # Change the string text between the quotation marks to see what the program does

# if string.isspace():
#     print("only white spaces")
	
# elif string.isalpha():
#     print("only letters")
	
# elif string.isdigit():
#     print("only digits")
	
# elif string.isalnum():
#     print("digits and letters")
	
# else:
#     print("digits, letters, and/or symbols")


# lst1 = list()
# print(lst1)

# lst2 = [ ]
# print(lst2)

# grocery_list = [ ]
# grocery_list.append("milk")
# grocery_list.append("eggs")
# grocery_list.append("bread")
# grocery_list.append("rice")
# print(grocery_list)
# print(len(grocery_list))


# grocery_list = ["milk", "eggs", "bread", "rice"]
# grocery_list.append(20.00)
# print(grocery_list)
# print(len(grocery_list))

# grocery_list = ["milk", "eggs", "bread", "rice", 20.00]
# print(grocery_list[0])
# print(grocery_list[1])
# print(grocery_list[2])
# print(grocery_list[3])
# print(grocery_list[4])

# grocery_list = ["milk", "eggs", "bread", "rice", 20.00]
# print(grocery_list)
# grocery_list[0] = "juice"
# print(grocery_list)

# my_list = [1, 2, 3, "Hello", "World"]
# print(my_list.pop())
# print(my_list)
# #print(last_item)

# my_list = [1, 2, 3, "Hello", "World"]

# my_list.insert(0,4)
# # inserts 4 to the front of my_list
# print(my_list)

# my_list.insert(3,"WORLD")
# # inserts "WORLD" to the 3rd index position
# print(my_list)

# my_list = [1, 2, 3, "Hello", "World"]
# print(my_list.clear())
# print(my_list)


# my_list = [1, 2, 3, "Hello", "World", 1, 1]

# print(my_list.count(1))          # in the list 3 times
# print(my_list.count("Hello"))    # in the list 1 time
# print(my_list.count("HELLO"))    # in the list 0 time (not in the list)

# string1 = "Helloworld"
# print(id(string1))
# string1 += "World"    # HelloWorld
# print(id(string1))


# lst = [1, 2, "a", "b"]
# print(id(lst))
# lst += ["hello", 5]
# print(id(lst))

# lst = [1, 2, "a", "b"]
# lst.extend(["hello", 5])
# print(lst)

# lst = [1, 2, 3]
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# lst3 = [1, 2, 3]

# print("\nConcatenating: +")
# print(id(lst1))
# lst1 = lst1 + lst
# print(id(lst1))

# print("\nMutating: +=")
# print(id(lst2))
# lst2 += lst2
# print(id(lst2))

# print("\nMutating: extend")
# print(id(lst3))
# lst3.extend(lst3)
# print(id(lst3))

# print("\nChecking the Values in the lists:\n")
# print(lst1)
# print(lst2)
# print(lst3)

# lst1 = [1, 2, 3, "Hello", "World"]    # original list
# lst2 = lst1                           # assignment operator
# lst3 = lst1[:]                        # slice copy
# lst4 = lst1.copy()                    # copy method

# print(lst2 is lst1)
# print(lst3 is lst1)
# print(lst4 is lst1)    #whereas lst3 and lst4, although they have the exact same values, they point to copies of the object. Basically, they are different list objects but have the same values stored in the collection.






# prime_numbers = []
# for i in range(1, 10, 2):
#     prime_numbers.append(i)
#     print(prime_numbers)


# lst1 = [1, 2, 3, "Hello", "World"]    # original list
# lst2 = lst1                           # assignment operator
# lst3 = lst1[:]                        # slice copy
# lst4 = lst1.copy()                    # copy method

# print(lst2 is lst1)
# print(lst3 is lst1)
# print(lst4 is lst1)

# lst1 = [1, 2, 3, "Hello", "World"]    # original list
# lst2 = lst1                           # assignment operator
# lst3 = lst1[:]                        # slice copy
# lst4 = lst1.copy()                    # copy method

# print("lst1 address:", id(lst1))
# print("lst2 address:", id(lst2))
# print("lst3 address:", id(lst3))
# print("lst4 address:", id(lst4))

##################### NESTED LISTS ################################
# nested_list = [[2, 4, 12], ["A", "B", "C"], [6.5, 4.2, 10.0]]
# print(nested_list[0])
# print(nested_list[1])
# print(nested_list[2])
# print(len(nested_list))

# nested_list = [[2, 4, 12], ["A", "B", "C"], [6.5, 4.2, 10.0]]
# print(nested_list[0][0])
# print(nested_list[1][1])
# print(nested_list[2][2])


# nested_list1 = [[2, 4, 12], ["A", "B", "C"], [6.5, 4.2, 10.0]]
# nested_list2 = nested_list1[:]
# nested_list3 = nested_list1.copy( )

# nested_list1[0][0] = 20
# nested_list2[1][1] = "D"
# nested_list3[2][2] = 40.0

# print(nested_list1)
# print(nested_list2)
# print(nested_list3)


# import copy

# nested_list = [[2, 4, 12], ["A", "B", "C"], [6.5, 4.2, 10.0]]
# nested_list_copy = copy.deepcopy(nested_list)

# # Check if the lists inside are the same object
# print("Using the is operator\n")
# print(nested_list[0] is nested_list_copy[0])
# print(nested_list[1] is nested_list_copy[1])
# print(nested_list[2] is nested_list_copy[2])

# Mutate those lists to make sure changes to one do not affect the other
#print("Mutating the lists\n")
# nested_list[0][0] = 10
# nested_list[0][1] = 20
# nested_list[0][2] = 30
# nested_list_copy[1][0] = "a"
# nested_list_copy[1][1] = "b"
# nested_list_copy[1][2] = "c"
# #print(nested_list)
# print(nested_list_copy)


############### WHILE LOOP #####################
# x = 5
# while x <= 100:
#     print(x)
#     if x == 95:
#         break 
#     x += 5
    
# x = 5
# while x <= 100:
#     print(x) 
#     x += 5
    

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)


# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")


# import random

# num = random.randint(1, 5)
# guess = int(input("Guess a number from 1 to 5!: "))

# while guess != num:
#     guess = int(input("Wrong guess. Try again!"))
	
# print("You guessed it correctly!")


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
# #   if x == "banana":
# #     break


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y) 

# string = "CHARACTERIZATION"
# for char in string:
#     print(char, end = "    ") #THE (end = " " ) syntax makes it print horizontally and not vertically

# beverages = ["water", "juice", "soda", "tea", "coffee"]

# for drink in beverages:
#     print(drink, end = ", ")



# Python program to 
# print Diamond shape 

# Function to print 
# Diamond shape 
# def Diamond(rows): 
# 	n = 0
# 	for i in range(1, rows + 1): 
# 		# loop to print spaces 
# 		for j in range (1, (rows - i) + 1): 
# 			print(end = " ") 
		
# 		# loop to print star 
# 		while n != (2 * i - 1): 
# 			print("*", end = "") 
# 			n = n + 1
# 		n = 0
		
# 		# line break 
# 		print() 

# 	k = 1
# 	n = 1
# 	for i in range(1, rows): 
# 		# loop to print spaces 
# 		for j in range (1, k + 1): 
# 			print(end = " ") 
# 		k = k + 1
		
# 		# loop to print star 
# 		while n <= (2 * (rows - i) - 1): 
# 			print("*", end = "") 
# 			n = n + 1
# 		n = 1
# 		print() 

# #Driver Code 
# #number of rows input 
# rows = 5
# Diamond(rows) 

# Program to print the given pattern 
# def print_asterisk(asterisk): 
# 	if (asterisk == 0): 
# 		return; 
# 	print("* ", end = ""); 
# 	print_asterisk(asterisk - 1); 

# def print_space(space): 
# 	if (space == 0): 
# 		return; 
# 	print(" ", end = ""); 
# 	print(" ", end = ""); 
# 	print_space(space - 1); 

# # function to print the pattern 
# def pattern(n, num): 
	
# 	# base case 
# 	if (n == 0): 
# 		return; 
# 	print_asterisk(n); 
# 	print_space(2 * (num - n) + 1); 
# 	print_asterisk(n); 
# 	print(""); 

# 	# recursively calling pattern() 
# 	pattern(n - 1, num); 

# # Driver Code 
# if __name__ == '__main__': 
# 	n = 5; 
# 	pattern(n, n); 

# # This code is contributed by Princi Singh 
for i in range(1, 20, 2):
    print(i, end = " ")
    if i == 15:
        break       