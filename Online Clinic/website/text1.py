import mysql.connector

db1=mysql.connector.connect(user='root', passwd='12345678',
                              host='localhost',
                              database='Book')
mycurs=db1.cursor()
q1=""
#mycurs.execute(q1)
print("IT Worked")