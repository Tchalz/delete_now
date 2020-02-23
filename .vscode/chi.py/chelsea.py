import pymysql.cursors
import random
connection = pymysql.connect(host='localhost', user='root', password='',
                             db='saturday_class', charset='', cursorclass=pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
    # sql_cmd = 'INSERT into strikers(fname, lname, age, nationality, position, race, email) values ("kanu", "nwankwo", 25, "nigerian", "centre_forward", "black", "kanu@gmail.com")'
    # cursor.execute(sql_cmd)
    # connection.commit()
    # print("jesus is lord")

    filename = "C:/Users/CHIBUZOR/Documents/my project/.vscode/chi.py/names.csv"
    raw_data = open(filename, "r").read()
    for name in raw_data.splitlines():

        f_name, l_name = name.split()
        base_email = "gmail.com"
        user_mail = f_name[:4] + l_name[:4]+base_email
        user_age = random.randint(10, 50)
    # if f_name.lower().startswith("e"):
        print(
            f" Firstname - {f_name}, lastname - {l_name}, mail - {user_mail}")
sql_cmd = f'INSERT into customer(lname, fname, age, mail) values ("{l_name}", "{f_name}", {user_age}, "{user_mail}")'

cursor.execute(sql_cmd)
connection.commit()
