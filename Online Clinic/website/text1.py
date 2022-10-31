import mysql.connector

db1=mysql.connector.connect(host="localhost",user="root",passwd="12345678")
mycurs=db1.cursor()
q1="CREATE DATABASE Book"
print("IT Worked")