import mysql.connector
from datetime import datetime

schooldb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "*********", #this is private for each person
    database = "schooldb"
    )

class Student():
    connection = schooldb
    cursor = schooldb.cursor()

    def __init__(self, studentNumber, name, surname, birtdate, gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birtdate = birtdate
        self.gender = gender
    
    def saveStudent(self):  #tek kayıt eklenir
        sql = "insert into students (studentNumber, name, surname, birthdate, gender) values (%s,%s,%s,%s,%s)"
        value = (self.studentNumber, self.name, self.surname, self.birtdate, self.gender)
        Student.cursor.execute(sql,value)

        try:
            schooldb.commit()
            print(Student.cursor.rowcount,"tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("hata", err)
        finally:
            schooldb.close()
    
    @staticmethod
    def saveStudents(liste):  #çoklu kayıt eklenir
        sql = "insert into students (studentNumber, name, surname, birthdate, gender) values (%s,%s,%s,%s,%s)"
        values = students
        Student.cursor.executemany(sql,values)

        try:
            schooldb.commit()
            print(Student.cursor.rowcount,"tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("hata", err)
        finally:
            schooldb.close()
    
    

# yusuf = Student("107","Yusuf","Büyükdağ",datetime(2005,7,11),"E")  ##1 kayıt eklendi
# yusuf.saveStudent()

#sql = "insert into students (studentNumber, name, surname, birthdate, gender) values (%s,%s,%s,%s,%s)"
students = (
    ("108", "Fatih", "Yılman", datetime(2005, 5, 11),"E"),
    ("109","İbrahim","Zan",datetime(2005, 6, 15),"E"),
    ("110","Halil","Kan",datetime(2005, 7, 12),"E"),
    ("111","Nihal", "Büyükdağ",datetime(2005, 9, 20),"K"),
    ("112", "Ahsen", "Söz",datetime(2004, 7, 21),"K"),
    ("113", "İrem", "Eren", datetime(2003, 8, 2),"K")
)
Student.saveStudents(students)

# cursor = schooldb.cursor()

# cursor.executemany(sql, students)

# try:
#     schooldb.commit()
#     print(cursor.rowcount, "tane kayıt eklendi.")
# except mysql.connector.Error as err:
#     print("hata", err)
# finally:
#     schooldb.close()


# print(schooldb)
# mycursor = schooldb.cursor()
# mycursor.execute("show databases")

# for i in mycursor:
#     print(i)
