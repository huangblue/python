# person.py
class Person:
    """Class to represent a person
    """
    def __init__(self):
        self.name =''
        self.age = 0
        
    def display(self):
        print("Person('%s','%d')" % (self.name, self.age))

    def __str__(self):
        return "Person('%s','%d')" % (self.name, self.age)
    
    def __repr__(self):
        return str(self)
