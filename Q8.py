import pymysql

def connection():
    try:
        conn = pymysql.connect(host="rds-demo.csaruqlxxway.us-east-1.rds.amazonaws.com",user="root",passwd="Borkar21",port=3306, db="Game_rahul" )
        print("connected.")
        return conn
    except Exception as e:
        print(e)

# prepare a cursor object using cursor() method
db = connection()
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   SEX CHAR(1),
   INCOME FLOAT )"""

cursor.execute(sql)
print("created table")
cursor.execute("INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('rahul', 'Meharkure', 21, 'M', 3000)")
cursor.execute("INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Akash', 'Mahale', 32, 'M', 2000)")
cursor.execute("INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Vishali', 'Shekhar', 20, 'F', 1000)")



cursor.execute("Select * from  EMPLOYEE")
results = cursor.fetchall()
print(results)

#delete

cursor.execute("DELETE FROM EMPLOYEE WHERE AGE < 25 ")

#update

cursor.execute("UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = 'M'")

print(cursor.execute("Select * from EMPLOYEE"))
results = cursor.fetchall()
print(results)

#select to see the update

cursor.execute("Select * from  EMPLOYEE")


db.commit()
# disconnect from server
db.close()
