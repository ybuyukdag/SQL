class Teacher():
 
    def __init__(self, id, branch, name, surname, birtdate, gender):
        if id is None:
            self.id=0
        else:
            self.id = id
        self.branch = branch
        self.name = name
        self.surname = surname
        self.birtdate = birtdate
        self.gender = gender
       