
from dbmanager import DBmanager 
from student import Student
import datetime

class App():
    def __init__(self):
        self.db = DBmanager()
    def initApp(self):
        msg = "-------\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Dersler\n7-Çıkış"

        while True:
            print(msg)
            islem = input("Seçiminiz: ")
            if islem == "1":
                self.displayStudents()
            elif islem == "2":
                self.addStudent()
            elif islem == "3":
                self.editStudent()
            elif islem == "4":
                self.deleteStudent()
            elif islem == "7":
                break
            else:
                print("Yanlış seçim")

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci Id:"))

        self.db.deleteStudent(studentid)

    
    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci Id:"))
        
        student =self.db.getStudentById(studentid)
        
        student[0].studentNumber = input("Öğrenci No: ") or student[0].studentNumber
        student[0].name = input("name: ") or student[0].name
        student[0].surname = input("surname: ") or student[0].surname
        student[0].gender = input("cinsiyet (E/K): ") or student[0].gender
        student[0].classid = input("sınıf: ") or student[0].classid

        year = input("yıl: ") or student[0].birthdate.year
        month = input("ay: ") or student[0].birthdate.month
        day = input("gün: ") or student[0].birthdate.day
        student[0].birthdate = datetime.date(year,month,day)
        self.db.editStudent(studentid)

    def addStudent(self):
        self.displayClasses()
        classid = int(input('hangi sınıf: '))
        
        number = input('Numara: ')
        name = input('Ad:')
        surname = input('Soyad:')
        year = int(input('Yıl:'))
        month = int(input('Ay:'))
        day = int(input('Gün:'))
        birthdate = datetime.date(year,month,day)
        gender = input("cinsiyet (E/K)")

        student = Student(None,number, name, surname, birthdate, gender, classid)
        self.db.addStudent(student)
    
    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(c.id,":", c.name)

    def displayStudents(self):
        self.displayClasses()
        classid = int(input('hangi sinif: '))
        students = self.db.getStudentByClassID(classid)
        print("Ogrenci Listesi")
        for std in students:
            print(std.id,"-",std.name,std.surname)
        return classid
 

app = App()
app.initApp() 

 

 

