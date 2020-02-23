"""
x = ["chibuzor", "chigozie", "chinyere", "kelechi", "ifeanyi"]
response = ""
while response != "end":
    response = input("enter item: ")
    if response in x:
        print("certainly")
    else:
        x.append(response)
        print(x)
"""

"""
x = [1, 2, 4, 5, 7, 8]

for item in x:
    sentence = "list contains " + str(item)
    print(sentence)

"""
"""
name = input("enter a name: ")
state = input("enter state: ")
current_location = input("enter current location: ")
user_sentence = "my name is {}, i come from {}, and am currently based in {}".format(
    name, state, current_location)
print(user_sentence)
"""

