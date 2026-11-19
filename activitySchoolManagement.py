class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  #private attribute

    def get_age(self):
        return self.__age  #safely accesses the private __age attribute


class Student(Person):
    def study(self):
        return f"{self.name} is studying"


#testing inherited features and the new study() method
student1 = Student("Lina", 20)
print(f"Name: {student1.name}")
print(f"Age: {student1.get_age()}")
print(student1.study())

#reflection: Accessing __age through get_age() protects the data from accidental
#or unauthorized changes (encapsulation) while still allowing safe, controlled read access.