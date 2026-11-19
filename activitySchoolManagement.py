class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age 
    
    def get_age(self):
        return self.__age 

Person1 = Person("Lina", 20) 
print(f"Name: {Person1.name}") 
print(f"Age: {Person1.get_age()}") 

# Reflection: Accessing __age through get_age() protects the data from accidental
# or unauthorized changes (encapsulation) while still allowing safe, controlled read access.