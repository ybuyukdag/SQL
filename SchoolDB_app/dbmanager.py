import mysql.connector
from datetime import datetime
from connection import connection
from student import Student
from teacher import Teacher
from Class import Class

class DBmanager():
    def __init__(self):
        self.connection  = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = "select * from student where id=%s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            std = self.cursor.fetchone()
            return Student.createStudent(std)
        except mysql.connector.Error as err:
            print("Hata:", err)

    def deleteStudent(self,studentid):
        sql = "delete from student where id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(self.cursor.rowcount,"tane kayıt silindi.")
        except mysql.connector.Error as err:
            print("hata", err)

    def getStudentByClassID(self,classid):
        sql = "select * from student where classid=%s"
        value = (classid,)
        self.cursor.execute(sql,value)
        try:
            std = self.cursor.fetchall()
            return Student.createStudent(std) 
        except mysql.connector.Error as err:
            print("Hata:", err)

    def getClasses(self):
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            cls = self.cursor.fetchall()
            return Class.CreateClass(cls) 
        except mysql.connector.Error as err:
            print("Hata:", err)
        
    def addStudent(self, student: Student):
        sql = "insert into student (studentNumber, name, surname, birthdate, gender, classid) values (%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber, student.name, student.surname, student.birtdate, student.gender,student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(self.cursor.rowcount,"tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("hata", err)

    def editStudent(self, student: Student):
        sql = "update student set studentNumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s, classid=%s where id=%s"
        value = (student.studentNumber, student.name, student.surname, student.birtdate, student.gender,student.classid,student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(self.cursor.rowcount,"tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("hata", err)
        pass
            
    def addTeacher(self, teacher: Teacher):
        pass
            
    def editTeacher(self, teacher: Teacher):
        pass

db = DBmanager()
#result = db.getStudentById(7)
result = db.getStudentByClassID(1)
# print(result.name)
# print(result.surname)
# print(result)
# print(result[0].name)
# print(result[0].surname)
# new_student = (None, "114","Yavuz", "Fatih",datetime(2005,3,31),"E",2)
# result = db.addStudent(new_student)

# print(result)
std = db.getStudentById(6)

print(std[0].birthdate)