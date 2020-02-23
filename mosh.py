'''
price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"down_payment: {down_payment}")
'''

'''
temperature = 50
if temperature > 30:
    print("a hot day")
else:
    print("its not a hot day")
'''

'''
name = "john smith"
if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("name must be a maximum of 50 characters")
else:
    print("name looks good")
'''


weight = int(input("weight: "))
unit = input("(L)bs or (K)g: ")
if unit == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight/0.45
    print(f" you are {converted} pounds")


# write a program to find the largest number in a list
'''
numbers = [3, 6, 2, 30, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# 2D list in python
'''
'''
matrix = [
    [1, 2, 3],  # [0]
    [4, 5, 6],  # [1]
    [7, 8, 9]  # [2]              #print(matrix[0][2])
]
for row in matrix:
    for item in row:
        print(item)
'''
'''
# list method
numbers = [5, 2, 1, 5, 5, 7, 4]
numbers.append(20)
numbers.insert(0, 10)
nummbers.remove(5)
numbers.clear()
numbers.pop()  # removes the last number that is 4
print(numbers)
print(50 in numbers)  # False cos 50 not in the list
print(numbers.count(5))  # 5 is counted 3 times in the list
print(numbers.sort())
numbers .index(5)    # 0, 3 and 4 that is where 5 is located
numbers.index(30)  # error cos 30 is not in the list

numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()

print(numbers)  # and not print(numbers.sort())
'''

# write a program to remove the duplicates in a list
'''
numbers = [2, 2, 4, 6, 3, 4, 6, 1, 4, 5, 6, 7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


# tuples
numbers = (1, 2, 3)
print(numbers[0])
'''
'''
# FOR LOOPS:
for item in range(100, 200, 5):
    print(item)


# program to calculate all the items in a shopping cart:
prices = [10, 20, 30]
total = 0
for item in prices:
    total += item
    print(f"total price: {total}")
'''