import MySQLdb

db = MySQLdb.connect ("localhost", "root", "tech@123", "python")

cursor = db.cursor()

sql = """INSERT INTO Employee ( Emp_no, Birth_Date, First_Name, \
         Last_Name, Gender, hire_date ) \
         values ( 1579010, '1968-07-17', "MAC", "MOHAN", "M", '1990-03-07' )"""


sql1 = """INSERT INTO Departments ( Emp_no, Department_Name ) \
          values ( 1579010, "QA" )"""

sql2 = """INSERT INTO Salaries ( Emp_no, Salary, From_Date, To_Date ) \
          values ( 1579010, 60000, '2018-06-01', '2018-07-02' )"""




try:
    cursor.execute(sql)
    print('1')
    cursor.execute(sql1)
    print('2')
    cursor.execute(sql2)
    print('3')


    db.commit()
    print ("sucessfull",cursor.rowcount)

except Exception as esc:
    print (esc)
    db.rollback()

db.close()