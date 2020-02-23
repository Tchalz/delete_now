import pymysql.cursors
import random
connection = pymysql.connect(host='localhost', user='root', password='',
                             db='saturday_class', charset='', cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:

#     prod_name = ["book", "biro", "calendar", "cleaner", "bags",
#                  "duster", "crayon", "table", "chair", "television"]
#     prod_prices = [random.randint(100, 5000) for i in range(10)]
#     prod_weight = [random.randint(10, 200) for i in range(10)]

#     for product in zip(prod_name, prod_prices, prod_weight):
#         name = product[0]
#         price = product[1]
#         weight = product[2]

#         sql_cmd = f' INSERT into product(name, price, weight) values ("{name}", "{price}", "{weight}")'
#         print(sql_cmd)

# #print(list(zip(prod_name, prod_prices, prod_weight)))







# for i in range(10):
#     sql_cmd = f'INSERT into orders(prod_id, cust_id, qty, order_date) values({random.randint(1, 15)}, {random.randint(2, 22)}, {random.randint(10, 200)}, "2020-{random.randint(1, 12)}-{random.randint(1, 31)}")'
#     print(sql_cmd)


# filename = 'C:/Users/CHIBUZOR/Documents/my project/.vscode/chi.py/charles.csv'
# raw_data = open(filename, 'r').read()
# for name in raw_data.splitlines():
#     f_name, l_name = name.split()
#     base_email = "@gmail.com"
#     usermail = f_name[:3] + l_name[:3] + base_email
#     user_age = random.randint(20, 50)
#     sql_cmd = f'INSERT into customer (fname, lname, age, email) values ("{f_name}", "{l_name}", "{user_age}", "{usermail}")'
#     print(f'FIRSTNAME:{f_name}, LASTNAME:{l_name}, AGE:{user_age}, EMAIL:{usermail}')
#     print(sql_cmd)





    cust_id = [random.randint(3, 28) for i in range(20)]
    prod_id = [random.randint(1, 25) for i in range(20)]
    qty = [random.randint(1, 50) for i in range(20)]
    order_date = ["{}-{}-{}".format(random.randint(2018, 2020), random.randint(1, 12), random.randint(1, 31)) for i in range(20)]

    for item in zip(cust_id, prod_id, qty, order_date):
        customer = item[0]
        product = item[1]
        qty = item[2]
        order_date = item[3]

        #print(product, customer, qty, order_date)
        sql_cmd = f' INSERT INTO orders(cust_id, prod_id, qty, order_date) values ("{customer}", "{product}", "{qty}", "{order_date}")'


        print(cust_id, prod_id, qty, order_date, sep = "\n")