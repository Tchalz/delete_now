
import pymysql.cursors
import random
import csv
connection = pymysql.connect(host='localhost', user='root', password='',
                             db='saturday_class', charset='', cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    # sql_cmd = 'INSERT into strikers(fname, lname, email, age, NATIONALITY) values ("kanu", "nwankwo", "kanu@gmail.com" , 25, "nigerian")'
    # cursor.execute(sql_cmd)
    # connection.commit()
    # print("jesus is lord")

    # MULTIPLE USER ADD FROM FILE

    #with connection.cursor() as cursor:
        ######### PRODUCT LIST ###############
        # sql_cmd = 'INSERT into student(stu_name, age, address, mail) values ("chibuzor nwozuzu", 25, "surulere lagos", "chibuzor_jonathan@yahoo.com")'
        #password = 'C:/Users/CHIBUZOR/Downloads/passwords(4).csv'
        #raw_data = open(password, "r").read()
        # print(password)

        filename = 'C:/Users/CHIBUZOR/Documents/my project/.vscode/chi.py/charles.csv'
        raw_data = open(filename, "r").read()
        password = 'C:/Users/CHIBUZOR/Downloads/passwords(4).csv'
        raw_data = open(password, "r").read()


        for name in raw_data.splitlines():

            f_name, l_name = name.split()
            base_email = "gmail.com"
            user_mail = f_name[:4] + l_name[:4]+base_email
            user_age = random.randint(10, 50)
            username = f_name
            balance = random.randint(10000, 1000000)

        # if f_name.lower().startswith("e"):
print(
    f" Firstname - {f_name}, lastname - {l_name}, mail - {user_mail}, username- {f_name}, balance - {balance}, password - {password}")
sql_cmd = f'INSERT into customer(lname, fname, age, mail) values ("{l_name}", "{f_name}", {user_age}, "{user_mail}")'

    # # cursor.execute(sql_cmd)
    # connection.commit()

    # with connection.cursor() as cursor:
    ######### PRODUCT LIST ###############
    # prod_name = ["book", "iron", "pen", "board", "slip", "clips", "staples","shoe"]
    # prod_prices = [random.randint(200, 500) for _ in range(8)]
    # prod_weight = [random.randint(10, 40) for _ in range(8)]
    # # # sql_cmd = 'INSERT into student(stu_name, age, address, mail) values ("chibuzor nwozuzu", 25, "surulere lagos", "chibuzor_jonathan@yahoo.com")'
    # print(list(zip(prod_name, prod_prices, prod_weight)))
    # for product in zip(prod_name, prod_prices, prod_weight):
    #      name = product[0]

    #      price = product[1]

    #      weight = product[2]

    #      sql_cmd = f'INSERT into product(name, price, weight) values ("{name}", "{price}", "{weight}")'
    #      print(sql_cmd)

    #      cursor.execute(sql_cmd)
    #      connection.commit()
    # for i in range(10):

    #     sql_cmd = f'INSERT into orders(prod_id, cust_id, qty, order_date) values ({random.randint(1,15)}, {random.randint(2,22)}, {random.randint(1,50)}, "2020-{random.randint(1,12)}-{random.randint(1,29)}")'
    #     print(sql_cmd)
    #     cursor.execute(sql_cmd)
    #     connection.commit()
