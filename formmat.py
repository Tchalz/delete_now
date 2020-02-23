
""""
list = [1, 3, 5, 7, 8, 9]
for x in list:
    sentence = "list contains " + str(x)
    print(sentence)
"""
'''
import range:

for i in range(11)
print(6)
'''



def chibuzor(*args):  # for multiple number of argument we introduce *args to our function
    number_list = args
    result_list = []
    for number in number_list:
        string = str(number)
        replaced = string.replace("234", "0")
        result_list.append(replaced)
    


variable = chibuzor("234894656478364", "234567588593354673",
         "23483544667383", "234844536478498")




#OOP allows us to represent real life objects as software objects
attributes of the objects
attributes and characteristics, behaviours and methods
