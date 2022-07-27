class Student:

    number_of_students = 0
    school = 'Online School'

    def __init__(self,first_name,last_name,majir):
        self.first_name = first_name
        self.las_name = last_name
        self.major = majir
        Student.number_of_students +=1

    def fullname_with_major(self):
        return f'{self.first_name}{self.las_name} is a {self.major}!'

    def fullname_with_major_school(self):
        return f'{self.first_name}{self.las_name} is a {self.major} going to {self.school}!'

    @classmethod
    def set_online_school(cls,new_school)-> "Student":
        cls.school = new_school

    @classmethod
    def split_student_str(cls,student_str)-> "Student":
        first_name,last_name,major= student_str.split('.')
        return cls(first_name,last_name,major)

    @staticmethod
    def my_static_method():
        print("Static method runs")


print(f'Number of Students={Student.number_of_students}')
#create few objects
student_1 = Student('Eric','Roby','CS')
student_1 = Student('John','Miller','Math')
print(student_1.school)
print(student_1.school)
print(f'Number of Students={Student.number_of_students}')
#instance method
print(student_1.fullname_with_major())
print(Student.fullname_with_major(student_1))

#classmethod
#explicit calling of classmethod
Student.set_online_school(Student,'Harvard')

#implicit calling of classmethod
Student.set_online_school('Harvard')

#static method calling
#it does not receive instance or class 
Student.my_static_method()

print(student_1.school)
print(student_1.school)
new_student = 'Gagan.Deep.DBMS'
student_3 = Student.split_student_str((new_student))

print(student_3.first_name)
print(student_3.las_name)
print(student_3.major)

