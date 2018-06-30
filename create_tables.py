import MySQLdb

db = MySQLdb.connect ("localhost", "root", "tech@123", "python")

cursor = db.cursor()
cursor.execute("drop tables if exists Employee , Departments , Salaries")

sql = """create table Employee ( Emp_no int(10) NOT NULL auto_increment primary key,\
         Birth_Date Date NOT NULL, First_Name varchar(14) NOT NULL, Last_Name varchar (10) NOT NULL,\
         Gender char(1) NOT NULL, hire_date date NOT NULL)"""

sql1 = """create table Departments ( Emp_no int(10) NOT NULL primary key, Department_Name varchar(30) NOT NULL)"""

sql2 = """create table Salaries ( Emp_no int(10) NOT NULL primary key, Salary int(10) NOT NULL, From_Date date NOT NULL, To_Date date NOT NULL )"""




try:
    cursor.execute(sql)
    cursor.execute(sql1)
    cursor.execute(sql2)


    db.commit()
    print ("sucessfull",cursor.rowcount)

except Exception as esc:
    print (esc)
    db.rollback()

db.close()