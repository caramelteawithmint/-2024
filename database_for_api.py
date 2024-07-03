from mysql.connector import connect
import pymysql
import pymysql.cursors
import getpass 
#from config import host, user, password, db_name 



try:
    with connect(
        host="localhost",
        user=input("Имя пользователя: "),
        password=getpass("Пароль: "),
        cursorclass=pymysql.cursors.DictCursor
    ) as connection:
        print ("Successfully connected")

except Exception as ex:    
    print("Connection refused..")
    print(ex)