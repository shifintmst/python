# class car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#     def display_info(self):
#         print(f"car:{self.make} {self.model} {self.year}")


# car1=car("honda","civic",2022)
# car1.display_info()
# car2=car("ford","mustang",2001)
# car2.display_info()          


# class employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary= salary

#     def display_employee(self):
#         print(f"name:{self.name}, salary:{self.__salary}")
#     def update_salary(self, new_salary):
#         self.__salary += new_salary
# emp = employee("john",50000)
# emp.display_employee()        
# emp.update_salary(10000)
# emp.display_employee()

# class animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         print(f"{self.name} make a sound.")
# class dog(animal):
#     def speak(self):
#         print(f"{self.name} says woof.")

# d = dog("buddy")
# d.speak()
# print(d.name)            

# from abc import ABC, abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
# rectangle = Rectangle(10,20)
# print(rectangle.area())           

# class Student:
#     def init(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display_grade(self):
#         if self.marks >= 90:
#             grade = 'A'
#         elif 75 <= self.marks < 90:
#             grade = 'B'
#         elif 50 <= self.marks < 75:
#             grade = 'C'
#         else:
#             grade = 'Fail'

#         print(f"Student Name: {self.name}, Grade: {grade}")


# # Create student objects
# student1 = Student("Alice", 85)
# student2 = Student("Bob", 45)

# # Call the display_grade method for each object
# student1.display_grade()
# student2.display_grade()

# class Student:
#  def __init__(self,name,marks):
#      self.name = name
#     self.marks = marks
#  def display_grade(self):
#     if self.marks >= 90:
#         grade = "A"
#     elif self.marks >= 75:
#         grade = "B"
#     elif self.marks >= 50:
#         grade = "c"
#     else:
#         grade = 'fail' 
#     print(f"student name: {self.name},grade: {grade}")                
# student1 = Student("shamal",95)
# student2 = Student("shifin",100)
# student1.display_grade()
# student2.display_grade()        