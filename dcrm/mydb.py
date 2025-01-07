import pymysql

try:
    dataBase = pymysql.connect(
        host="localhost",
        user="root",
        password="Jan@2025_",
        database="elderco"
    )
    print("Connected to the database")
except Exception as e:
    print("Error while connecting to MySQL", e)
finally:
    if 'dataBase' in locals():
        dataBase.close()
        print("MySQL connection is closed")
