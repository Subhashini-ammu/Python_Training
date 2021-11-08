import mysql.connector
db = mysql.connector.connect(host="localhost", user="root", password="subhashini@98", database="demo")
curzor = db.cursor()
x = curzor.execute("select * from table1")
y = curzor.fetchall()
print(y)