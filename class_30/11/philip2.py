import pymysql.cursor
connection = pymysql.connect(host='localhost', user='root', password='',
                             db='football-club', charset='', cursorclass=pymysql.cursor.Dictcursor)
with connection.cursor() as cursor:
    sql_cmd = 'INSERT into student(stu_name, age, address, email) values ("chibuzor nwozuzu", 25, "surulere lagos", "chibuzor_jonathan@yahoo.com")'
    cursor.execute(sql_cmd)
    connection.commit()
