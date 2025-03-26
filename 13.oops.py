'''                 object oriented programming                        '''
# class(template)
'''
1.we will define class by using 'class' keyword
2.class is a blue print to create a objects
3.collection of objects is called class
Example : fruits,cars,students
'''
##----------------------------------------------------------------
# object->in python everything is an object.including list,strings,integers,functions,etc
# physical entity(real)
'''
1.an instance of a class . Instance is a specific object created form class
2.memory is created when it declared
ex apple,orange,mango-tata,mahindra,bmw-easwer,sai,jagadish,---
'''
##----------------------------------------------------------------
# class Easwer():# class defination
#     # constructors
#     # functions
#     # variables
##----------------------------------------------------------------
# attributes / (variables)/ data members
'''
age=20 
color='blue'
'''
##----------------------------------------------------------------
# method(behaviour) / functions / member functions
'''
eat() 
sleep()
'''
##----------------------------------------------------------------

# class Easwer(): # class defination
#     a=10 # attribute/variable
#     b="Ram"
#     def ClassMethod(self):
#         print("this is class")
#         print(self.a)
# # Obj name=Class name()
# obj1=Easwer() #object declaration,we can create n number of objects as we want
# obj2=Easwer() # creating another object declaration for testing
# obj1.ClassMethod() 
# obj2.ClassMethod()
# print(obj1.b)
# print(obj2.b)
##----------------------------------------------------------------

# self keyword
'''
using self we can access the attributes and methods of the class(current class only)
'''
# class Easwer(): # class defination
#     def Output(self):
#         print("this is class")

# # object name = class name() object creation
# selftest=Easwer()
# selftest.Output() # methods access-> object_name.method

##----------------------------------------------------------------
#using self keyword we can access the attributes and methods of the class
# class Shiva():
#     a=10 
#     b=20
#     def view(self):
#         print("This is view class")
#         print(self.b)
#     def show(self):
#         print("this is class")
#         self.view()  # calling another method using self keyword
#         return("this is easwer")    
# Rama=Shiva()    #obj name=class name()
# print(Rama.a)
# Rama.show()    
# print(Rama.show())
##----------------------------------------------------------------
# '''In Python the __init__() method is called the constructor
# and is always called when an object is created
# Constructors are generally used for instantiating an object. 
# The task of constructors is to initialize(assign values)to the attributes(variables)data members
# of the class when an object of the class is created.
# doesn't support multiple constructor'''
##----------------------------------------------------------------
# class Person:
#     def __init__(self):  # No parameters except self
#         print("A new person object is created.")
# p = Person() 
##----------------------------------------------------------------
# class Easwer():
#     def __init__(self,a,b,c): #__init__ method is called automatically when obj creates
#         self.a=a
#         self.bb=b
#         self.ccc=c
#         print(a,c,b,a,b,c)
#     def Output(self):
#         print(self.a,self.bb,self.ccc)
# p=Easwer(1,2,3) #creating an object(instance) to a class is instantiation
# p.Output()
# q=Easwer(5,6,7)
# q.Output()
##----------------------------------------------------------------

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand  # Initializing instance variable
#         self.model = model
#     def show_details(self):
#         print(f"Car Brand: {self.brand}, Model: {self.model}")

# # Creating an object (constructor runs automatically)
# my_car = Car("Toyota", "Corolla") 
# my_car.show_details()
#__init__() runs when Car("Toyota", "Corolla") is created.

# It initializes attributes (self.brand, self.model).

##----------------------------------------------------------------
#Using self we also create and store an object of a different class inside another class.
# class Engine:
#     def start(self):
#         print("Engine is starting...")

# class Car:
#     def __init__(self):  # Constructor runs automatically when an object is created
#         self.engine = Engine() # Creating an diff class Engine object inside Car class

#     def drive(self):
#         self.engine.start()  # Calling Engine's method using self
#         print("Car is driving.")

# # Creating a Car object
# my_car = Car()  # This runs __init__()
# my_car.drive()  # Calls drive(), which calls engine.start()

##----------------------------------------------------------------

# class Easwer():
#     def __init__(self,a,b,c):
#         self.easwer=a
#         self.sai=b
#         self.jagadish=c
#     def esj(self):
#         print(self.easwer,self.sai,self.jagadish)

# e=Easwer(1,2,3)
# e.esj()

##----------------------------------------------------------------

# class Mobiles():
#     def __init__(self,Mobile_name,Mobile_Ram,Mobile_battery,Mobile_Price):
#         self.a=Mobile_name
#         self.c=Mobile_Ram
#         self.d=Mobile_battery
#         self.e=Mobile_Price
#         print(Mobile_name,Mobile_Ram,Mobile_battery,Mobile_Price)  
#     def Mobile_Data(self):
#         print("Mobile Name:",self.a)
#         print("Mobile Ram:",self.c)
#         print("Mobile Battery:",self.d)
#         print("Mobile Price:",self.e)
# while True:
#     name=input("Enter the Mobile Name:")
#     ram=input("Enter the Mobile Ram:")
#     battery=input("Enter the Mobile Battery:")
#     Price=float(input("Enter the Mobile Price:"))
#     if name.lower() == 'done':
#         break
#     Mobile_obj=Mobiles(name,ram,battery,Price)
#     Mobile_obj.Mobile_Data()

##----------------------------------------------------------------

# INHERITANCE
# single (parent child)
# # multiple(two are more parent/base classes to 1 child)
# # # hierarchical(Tree structure - one parent/base class with more sibiling childs)
# # # # multilevel(level by level -> grand father,father,song,grandson)

##----------------------------------------------------------------
## Single inheritance

# class Parent:
#     def output(self): 
#         print('this is parent class')
# class Child(Parent):
#     def outputChild(self): # output
#         print('this is child class')
# Si=Child()
# Si.output() 
# Si.outputChild()
##----------------------------------------------------------------
## Single inheritance
# class Person:           # Parent class
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f"Name: {self.name}")

# class Student(Person):      # Child class (Inheriting from Person)
#     def __init__(self, name, age, roll_number, marks):
#         super().__init__(name, age)      # Calling the Parent class constructor
#         self.roll_number = roll_number
#         self.marks = marks
#     def display_student(self):
#         self.display()          # Calling the Parent class method
#         print(f"Age: {self.age} ,Roll Number: {self.roll_number}, Marks: {self.marks}")

# student1 = Student("Easwer", 33, 10, 92)     # Creating an object of Student
# student1.display_student()      # Calling method

##----------------------------------------------------------------
## Multiple inheritance (Morethan 1 base/parent class)
# class Father:
#     def F(self):
#         print('this is Father class')
# class Mother:
#     def M(self):
#         print('this is Mother class')
# class Brother:
#     def B(self):
#         print("this is brother class")

# class Child(Father,Mother,Brother):
#     def C(self):
#         print('this is Child class')      
# MI=Child()
# MI.F()
# MI.M()
# MI.B()
# MI.C()

##----------------------------------------------------------------

# Multiple Inheritance -> Employee Management System
# class Person:       # Parent class 1: Person (Stores basic details)
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display_personal_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
# class Job:          # Parent class 2: Job (Stores job-related details)
#     def __init__(self, job_title, salary):
#         self.job_title = job_title
#         self.salary = salary
#     def display_job_info(self):
#         print(f"Job Title: {self.job_title}, Salary: {self.salary}")
# class Employee(Person, Job):    # Child class: Employee (Inherits from both Person and Job)
#     def __init__(self, name, age, job_title, salary, employee_id):
#         Person.__init__(self, name, age)# Calling constructors of both parent classes using class name
#         Job.__init__(self, job_title, salary)
#         self.employee_id = employee_id  # Additional attribute for Employee
#     def display_employee_info(self):
#         self.display_personal_info()  # Calling Person's method
#         self.display_job_info()  # Calling Job's method
#         print(f"Employee ID: {self.employee_id}")
# emp1 = Employee("Easwer", 33, "Software Engineer", 100000, "E10")    # Creating an Employee object
# emp1.display_employee_info()    # Displaying employee details

##----------------------------------------------------------------
## Multi level Inheritance(GF->F->C)
# class testing:
#     def __init__(self):
#         print("Testing __init__ , without calling")
# class GrandFather(testing):
#     def outputGF(self):
#         print('this is GRAND FATHER class')
# class Father(GrandFather):
#     def outputF(self):
#         print('this is Father class')
# class Child(Father):
#     def outputC(self):
#         print('this is Child class')      
# C=Child()
# C.outputGF()
# C.outputF()
# C.outputC()
##----------------------------------------------------------------
## Multi level Inheritance -> Corporate Employee Hierarchy
# class Person:       # Base class
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display_personal_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
# class Employee(Person):     # Intermediate class (inherits from Person)
#     def __init__(self, name, age, employee_id, department):
#         super().__init__(name, age)  # Calls Person's constructor
#         self.employee_id = employee_id
#         self.department = department
#     def display_employee_info(self):
#         self.display_personal_info()  # Calling Person's method
#         print(f"Employee ID: {self.employee_id}, Department: {self.department}")
# class Manager(Employee):    # Derived class (inherits from Employee)
#     def __init__(self, name, age, employee_id, department, team_size):
#         super().__init__(name, age, employee_id, department)  # Calls Employee's constructor
#         self.team_size = team_size
#     def display_manager_info(self):
#         self.display_employee_info()  # Calling Employee's method
#         print(f"Team Size: {self.team_size}")
# manager1 = Manager("Easwer", 33, "E10", "IT", 10)   # Creating a Manager object
# manager1.display_manager_info() # Displaying details

##----------------------------------------------------------------
# Hierarical Inheritance
# class Father:#150cr
#     def outputF(self):
#         print('this is father class')
# class Child1(Father):#50cr
#     def outputc1(self):
#         print('this is child 1 class')
# class Child2(Father):#50cr
#     def outputc2(self):
#         print('this is child  2 class')    
# class Child3(Father):#50cr
#     def outputc3(self):
#         print('this is child  3 class')     
# c1=Child1()
# c2=Child2()
# c3=Child3()
# c1.outputc1()
# c2.outputc2()
# c3.outputc3()
# c3.outputF() 
# c2.outputF() 
##----------------------------------------------------------------
# Hierarchial Inheritance -> University System
# class Person:       # Parent class
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display_personal_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
# class Student(Person):      # Child class 1: Student (Inherits from Person)
#     def __init__(self, name, age, student_id, course):
#         super().__init__(name, age)  # Calling Person's constructor
#         self.student_id = student_id
#         self.course = course
#     def display_student_info(self):
#         self.display_personal_info()  # Calling method from Person
#         print(f"Student ID: {self.student_id}, Course: {self.course}")
# class Teacher(Person):      # Child class 2: Teacher (Inherits from Person)
#     def __init__(self, name, age, teacher_id, subject):
#         super().__init__(name, age)  # Calling Person's constructor
#         self.teacher_id = teacher_id
#         self.subject = subject
#     def display_teacher_info(self):
#         self.display_personal_info()  # Calling method from Person
#         print(f"Teacher ID: {self.teacher_id}, Subject: {self.subject}")
# student1 = Student("Easwer", 33, "E110", "Computer Science")     # Creating Student object
# teacher1 = Teacher("Mr.RAM", 45, "T202", "Mathematics")       # Creating Teacher object
# print("\nStudent Details:")         
# student1.display_student_info()
# print("Teacher Details:")
# teacher1.display_teacher_info()


##----------------------------------------------------------------

# Polymorphism      poly-many       morph = forms
##----------------------------------------------------------------
# 1.method overloading 
# class Methodoverlod:

#     def something(self,a=None,b=" ",c=[]): #a->None is commonly used, b->in string here we use empty space.
#         print(a,b,c)
# obj=Methodoverlod()
# obj.something(1,2,3)
# obj.something(1,2)
# obj.something(1)
# obj.something()
##----------------------------------------------------------------
# Method overloading
# Same method name book_ticket(), different behaviors!
# This is method overloading behavior using default arguments.

# class MovieTicket:
#     def book_ticket(self, movie_name, seats=1, discount=None):
#         if discount:
#             print(f"Booking tickets {seats} for {movie_name} with a {discount}% discount.")
#         else:
#             print(f"Booking tickets {seats} for {movie_name}.")

# ticket = MovieTicket()      # Creating an object

# ticket.book_ticket("Inception")     # Booking a single ticket (Default seats = 1)

# ticket.book_ticket("Avengers", 3)   # Booking multiple tickets

# ticket.book_ticket("Interstellar", 2, 10)   # Booking with a discount

# ##----------------------------------------------------------------
# # 2.method overridding

# class Methodoverride:
#     def display(self):
#         print("this is parent class")
# class Child(Methodoverride):
#     def display(self):
#         print("this is child class")
#         super().display()                
# obj=Child()
# obj.display()
##----------------------------------------------------------------

# class PaymentMethod:        ##  Polymorphism -> Payment Processing System
#     def make_payment(self, amount):
#         pass  # This is a placeholder (to be overridden)
# class CreditCard(PaymentMethod):        # Subclass 1: Credit Card Payment
#     def make_payment(self, amount):
#         print(f"Processing credit card payment of Rs.{amount}")
# class PayPal(PaymentMethod):            # Subclass 2: PayPal Payment
#     def make_payment(self, amount):
#         print(f"Processing PayPal payment of Rs.{amount}")
# class UPI(PaymentMethod):           # Subclass 3: UPI Payment
#     def make_payment(self, amount):
#         print(f"Processing UPI payment of Rs.{amount}")
# def process_payment(payment_method, amount):    # Function to process payment using polymorphism
#     payment_method.make_payment(amount)
# credit_card = CreditCard()          # Creating objects of different payment methods
# paypal = PayPal()
# upi = UPI()
# print("Customer chooses Credit Card:")  # Processing payments using different methods
# process_payment(credit_card, 1000)
# print("Customer chooses PayPal:")
# process_payment(paypal, 500)
# print("Customer chooses UPI:")
# process_payment(upi, 300)

##----------------------------------------------------------------

#encapsulation hides the internal details of an object and only allowing access to what’s necessary.
#This ensures data security, prevents accidental modification, and improves code maintainability
# # public, private __ ,protected _
##----------------------------------------------------------------
# class GFather:
#     def __init__(self,a,b):
#         self._y=a #  self._y is protected (_ is protected), available to all classes
#         self.__z=b # self.__z is private   (__ is private), available to this class only
#         print(self._y)
#         print(self.__z)
# class Father(GFather):
#     def display1(self):
#         print(self._y)
#         ##print(self.__z) # __z is private, it has no access to parent class
# class Child2(Father):
#     def display2(self):
#         print("child2", self._y)
# obj=Child2(10,92)
# obj.display2()
# obj.display1()
##----------------------------------------------------------------
# class BankAccount:      #Encapsulation in Banking System
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.__balance = balance  # Private attribute (Encapsulation)
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Rs.{amount} deposited. New balance: Rs.{self.__balance}")
#         else:
#             print("Invalid deposit amount.")
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Rs.{amount} withdrawn. Remaining balance: Rs.{self.__balance}")
#         else:
#             print("Insufficient balance or invalid amount.")
#     def get_balance(self):
#         return self.__balance  # Controlled access to balance
# account = BankAccount("1234567890", 5000)       # Creating an account
# account.deposit(2000)       # Depositing money
# account.withdraw(3000)      # Withdrawing money
# # Trying to access the private attribute directly (Will not work)
# #print(account.__balance)  # ❌ AttributeError: 'BankAccount' object has no attribute '__balance'
# print("Current Balance:", account.get_balance())# Correct way to access balance using public method

##----------------------------------------------------------------

# a=10
# def func():
#     b=20
#     print('this is fun',b,a)
# func()

# print(a)

##----------------------------------------------------------------

# #  Abstraction ->  hides implementation details
# #abstract method there is no body
# #abstract base class can not  create object
# #a class contain one or more abstract methods then it said to be a abc
# from abc import ABC, abstractmethod   
# class Car(ABC):          # parent/base class can't create object
#     @abstractmethod      #decorator,now mileage get abstract method properties 
#     def mileage(self):   #abstract method has no body
#         pass             #implementation details available only in subclasses
# class Tesla(Car):   
#     def mileage(self):   
#         print("The mileage is 30kmph")   
# class Suzuki(Car):   
#     def mileage(self):   
#         print("The mileage is 25kmph ")   
# t= Tesla ()   
# t.mileage()   
# s = Suzuki()   
# s.mileage()   

##----------------------------------------------------------------

# from abc import ABC, abstractmethod

# class Payment(ABC):  # Abstract class
#     @abstractmethod
#     def process_payment(self, amount):
#         pass  # No implementation (must be defined in subclasses)

# class CreditCard(Payment):  
#     def process_payment(self, amount):  
#         print(f"Processing credit card payment of Rs.{amount}")

# class PayPal(Payment):  
#     def process_payment(self, amount):  
#         print(f"Processing PayPal payment of Rs.{amount}")
# # Creating objects
# credit = CreditCard()
# paypal = PayPal()
# # Calling the abstract method implementation
# credit.process_payment(1000)  #  Processing credit card payment
# paypal.process_payment(500)  #  Processing PayPal payment

# payment = Payment()  # ❌ ERROR: Cannot instantiate an abstract class

##----------------------------------------------------------------
# Restaurant ordering system

# from abc import ABC, abstractmethod
# class Restaurant(ABC):      # Abstract class
#     @abstractmethod
#     def prepare_food(self, food_item):
#         pass  # Abstract method (must be implemented by child classes)
# class IndianRestaurant(Restaurant):     # Subclass 1: Indian Restaurant
#     def prepare_food(self, food_item):
#         print(f"Preparing {food_item} with Indian masala and curry.")
# class ItalianRestaurant(Restaurant):    # Subclass 2: Italian Restaurant
#     def prepare_food(self, food_item):
#         print(f"Preparing {food_item} with Italian spices and cheese.")
# def order_food(restaurant, food_item):  # Function to order food from a restaurant
#     restaurant.prepare_food(food_item)  # Calls the appropriate subclass method
# indian = IndianRestaurant()
# italian = ItalianRestaurant()
# print("Customer orders food from an Indian restaurant:")
# order_food(indian, "Biryani")
# print("Customer orders food from an Italian restaurant:")
# order_food(italian, "Pasta")

##----------------------------------------------------------------

