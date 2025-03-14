class student:

    def __init__(self):         #we use innit because when object is initialized it should be a dictionary
        
        self.student = {}

    def add_data(self, name, age , mark):

        self.name = name

        self.age = age

        self.mark = mark

        self.student[name] = {"age": age, "mark": mark}

        print(self.student)

    def up_mark(self,name,u_mark):

        self.student[name]["mark"] = u_mark

        print(self.student)



obj = student()

obj.add_data(name="Sangee", age=26,mark=99)