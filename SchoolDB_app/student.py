class Student:
 
    def __init__(self, id, studentNumber, name, surname, birthdate, gender,classid):
        if id is None:
            self.id=0
        else:
            self.id = id
        self.studentNumber = studentNumber
        if len(name) > 45:
            raise Exception("Name için maksimum 45 karakter girilebilir")
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.classid = classid

    @staticmethod
    def createStudent(std):
        list=[]
        if isinstance(std, tuple):
            list.append(Student(std[0],std[1],std[2],std[3],std[4],std[5],std[6]))
        else:
            for i in std:
                list.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        return list

