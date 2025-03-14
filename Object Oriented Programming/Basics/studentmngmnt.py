# student management system      #  {}
# add_a_student(id,name,age,grade)   {1:{"name":name,"age":age,"grade":grade}}
# delete a student
# display a student details
# update grade of a student




class Student():

    def __init__(self):

        self.student = {}

    def add_student(self,id,name,age,grade):

        self.id = id

        self.name = name

        self.age = age

        self.grade = grade

        self.student[id]= {"name":name,"age":age,"grade":grade}

        print(self.student)

    def remove_student(self,id):

        if  id in self.student:

            self.student.pop(id)

            print("removed succesfully",self.student)

            

        else:

            print("failed to remove")

    def update_student(self,id,grade):

        if id in self.student:

            self.student[id]["grade"]=grade

            print("updated succesfully")

        else:

            print("failed to update")


obj = Student()

obj.add_student(id=1,name="sangee",age=56,grade="a")

obj.add_student(id=2,name="DJnago",age=6,grade="z")

obj.remove_student(2)
