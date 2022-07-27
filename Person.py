from operator import ge


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person{self.name},{self.age} years old"
    
    def __repr__(self):
        return f"<Person('{self.name}',{self.age})>"

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')

obj = Person('bob',34)
print(obj)
del obj