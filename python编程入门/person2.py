# person2.py
class Person:
    def __init__(self, name ='',age = 0):
        self.__name = name
        if 0<age<=150:
            self.__age = age
        else:
            self.__age=0
        
    @property#装饰器 获取函数
    def name(self):       
        return self.__name

    @property#装饰器 获取函数
    def age(self):       
        return self.__age

    @age.setter#装饰器 设置函数
    def age(self, age):        
        if 0 < age <= 150:
            self.__age = age
            
    @name.setter#装饰器 设置函数
    def name(self, name):        
        self.__name = name
            

    def display(self):
        print(self)

    def __str__(self):
        return "Person('%s', %s)" %(self.__name, self.__age)

    def __repr__(self):
        return str(self)
