import mysql.connector
import pymysql
import pymysql.cursors
import getpass 
#from config import host, user, password, db_name 



try:
    connection = pymysql.connect(
        host="localhost",
        user=input("Имя пользователя: "),
        password=getpass("Пароль: "),
        cursorclass=pymysql.cursors.DictCursor
    )
    print ("Successfully connected")
except Exception as ex:    
    print("Connection refused..")
    print(ex)