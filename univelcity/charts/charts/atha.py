

import pymysql.cursors
import random
connection = pymysql.connect(host='localhost', user='root', password='',
                             db='football-clubs', charset='', cursorclass=pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
    sql_cmd = 'INSERT into student(stu_name, age, address, email) values ("chibuzor nwozuzu", 25, "surulere lagos", "chibuzor_jonathan@yahoo.com")'
    cursor.execute(sql_cmd)
    connection.commit()
print("done")

# MULTIPLE USER ADD FROM FILE
'''
with connection.cursor() as cursor:
    sql_cmd = 'INSERT into student(stu_name, age, address, email) values ("chibuzor nwozuzu", 25, "surulere lagos", "chibuzor_jonathan@yahoo.com")'

    filename = 'C:/Users/CHIBUZOR/Documents/my project/.vscode/chi.py/charles.csv'
    raw_data = open(filename, "r").read()
    for name in raw_data.splitlines():
        f_name, l_name = name.split()
        base_email = "gmail.com"
        user_mail = f_name[:4] + l_name[:4]+base_email
        user_age = random.randint(10, 50)
        # if f_name.lower().startswith("e"):
        print(
            f" Firstname - {f_name}, lastname - {l_name}, Email - {user_mail}")
        sql_cmd = f'INSERT into student(stu_name, age, address, email) values ("{name}", {user_age}, "lagos", "{user_mail}")'
        cursor.execute(sql_cmd)
        connection.commit()
'''
