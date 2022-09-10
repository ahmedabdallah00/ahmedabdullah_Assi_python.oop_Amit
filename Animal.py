class Animal:
    
    num=0

    def __init__(self,age1,name1):
        self.age = age1
        self.name =name1
        Animal.num+=1
    
    def set_name(self,name):
        self.name = name
    
    def set_age(self,age):
        self.age = age
    
    def get_name(self):
        return self.name 
    
    def set_age(self):
        return self.age 

    def print_num(self):
        print('number of elements of class is'+Animal.num)    

dog =Animal(15,"ahmed")
print(dog.age,dog.name)