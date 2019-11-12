# person1.py
class Person:
    """Class to represent a person
    """

    def set_age(self,age):
        if 0<age<150:
            self.age=age
            
    #在这个函数中表现
    def __init__(self,name,age):#,name='',age=0
        self.name = name
        self.age = age
        
    def display(self):
        print("Person('%s',%d)" % (self.name, self.age))

    def __str__(self):
        return "Person('%s',%d)" % (self.name, self.age)
    
    def __repr__(self):
        #return str(self)
        return "Person('%s',%d)" % (self.name, self.age)
