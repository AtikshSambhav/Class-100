#1)creating blueprint-class 
class Student(object):

    #Properties or Attributes
    def __init__(self,name,age,grade,city):
        self.name=name
        self.age=age
        self.grade=grade
        self.city=city

    #function or methods
    def greeting(self):
        print("Hi Student !",self.name)

    def hobby(self):
        print('Playing game')

#2)creating Objects for class
student1=Student("Atiksh",13,9,"Nagpur")
student2=Student("Saksham",12,7,"Napur")

print(student2.greeting())


    


    

        
