class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  #private attribute

    def get_age(self):
        return self.__age  #safely accesses the private __age attribute


class Student(Person):
    def study(self):
        return f"{self.name} is studying"


class Teacher(Person):
    def teach(self):
        return f"{self.name} is teaching"


#Exercise 3
student1 = Student("Lina", 20)
print(f"Name: {student1.name}")
print(f"Age: {student1.get_age()}")
print(student1.study())

print()

#Exercise 4
teacher1 = Teacher("Mona", 30)
print(f"Name: {teacher1.name}")
print(f"Age: {teacher1.get_age()}")
print(teacher1.teach())

# Reflection: Accessing __age through get_age() protects the data from accidental
# or unauthorized changes (encapsulation) while still allowing safe, controlled read access.