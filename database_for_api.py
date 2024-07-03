from mysql.connector import connect, Error
import pymysql
import pymysql.cursors
import getpass 
#from config import host, user, password, db_name 



try:
    with connect(
        host="localhost",
        user=input("Имя пользователя: "),
        password=getpass.getpass("Пароль: "),
        #cursorclass=pymysql.cursors.DictCursor
    ) as connection:
        create_db_query = "CREATE DATABASE head_hunter_vacancy"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
        print ("Successfully connected")

except Exception as ex:    
    print("Connection refused..")
    print(ex)


try:
    with connect(
        host="localhost",
        user=input("Имя пользователя: "),
        password=getpass.getpass("Пароль: "),
        #cursorclass=pymysql.cursors.DictCursor
    ) as connection:
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
        print ("Successfully connected")

except Error as e:    
    print("Connection refused..")
    print(e)

create_vacancies_table_query = """
CREATE TABLE vacancies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    vacancies_id_list VARCHAR(100)
    area_list VARCHAR(100)
    scedule_list VARCHAR(100)
    professional_roles_list VARCHAR(100)
    employment_list VARCHAR(100)
    experience_list VARCHAR(100)
) """

with connection.cursor() as cursor:
    cursor.execute(create_vacancies_table_query)
    connection.commit()