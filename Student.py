class Students:
    num_of_students =0
    def __init__(self,age1,name1,num_of_course1):
        self.age = age1
        self.name = name1
        self.num_of_course = num_of_course1
        Students.num_of_students +=1


    def info_student(self):
        print("age: " + str(self.age)+' name: ' + self.name+' num of course: '+ self.num_of_course)  

ahmed=Students(15,'ahmed','20')
ahmed.info_student()          
