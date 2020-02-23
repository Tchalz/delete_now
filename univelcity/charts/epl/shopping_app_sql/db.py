import pymysql.cursors
import random
import datetime
import env_variables as variables
# from .env_variables import ENV_DATA, db_host, db_password   #optional depending on env file interation method usage

connection = pymysql.connect(host=variables.db_host, user=variables.db_username, password=variables.db_password,
                             db=variables.db_name, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:

    ########################## CREATE USER TABLE AND POPULATE USER TABLE ############################################################

    #sql_cmd = "CREATE TABLE IF NOT EXISTS user (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, fname VARCHAR(20), lname VARCHAR(20), age INT(4), username VARCHAR(20), password VARCHAR(20), balance BIGINT, email VARCHAR(30))"
    sql_cmd = f'INSERT into USER(fname, lname, age, username, password, balance, mail) values ("{f_name}", "{l_name}", {user_age}, "{username}",{password}, {balance})'
    #password = 'C:/Users/CHIBUZOR/Downloads/passwords(2).csv'
    filename = 'C:/Users/CHIBUZOR/Documents/my project/.vscode/chi.py/charles.csv'
    raw_data = open(password, "r").read()
    #raw_data = open(filename, "r").read()

    for passwords in raw_data.splitlines():

        f_name, l_name = name.split()
        base_email = "gmail.com"
        user_mail = f_name[:4] + l_name[:4]+base_email
        user_age = random.randint(10, 50)
        username = f_name
        balance = random.randint(10000, 1000000)

    print(
        f" Firstname - {f_name}, lastname - {l_name}, mail - {user_mail}, username- {f_name}, balance - {balance}, password - {password}")
    sql_cmd = f'INSERT into customer(lname, fname, age, mail) values ("{l_name}", "{f_name}", {user_age}, "{user_mail}")'

    print(f" Firstname - {f_name}, lastname - {l_name}, mail - {user_mail}, age-{user_age}, username-{username}, password-{password}, Balance-{balance}")
    # cursor.execute(sql_cmd)
    # connection.commit()
    print("SUCCESSFULLY CREATED TABLE user")

    # CREATE PRODUCTS TABLE #######################################################3

    sql_cmd = "CREATE TABLE IF NOT EXISTS product (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(20), brand VARCHAR(20), price INT(9), weight INT(6))"
    
    cursor.execute(sql_cmd)
    connection.commit()
    print("successfully created products table")

    # ############################### CREATE CART TABLE ####################################################

    sql_cmd = "CREATE TABLE IF NOT EXISTS cart (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, user_id INT, FOREIGN KEY(user_id) REFERENCES user(id), product_id INT, FOREIGN KEY(product_id) REFERENCES product(id), qty INT(6))"

    print("successfully created cart table")
    # cursor.execute(sql_cmd)
    # connection.commit()

    # ############################### CREATE ORDERS TABLE ###################################################

    sql_cmd = "CREATE TABLE IF NOT EXISTS orders (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, user_id INT, FOREIGN KEY(user_id) REFERENCES user(id), product_id INT, FOREIGN KEY(product_id) REFERENCES product(id), qty INT(6), order_date DATE())"

    print("successfully created orders table")
    # cursor.execute(sql_cmd)
    # connection.commit()
