# def Easwer(a,b):
#     print(a+b)

# while True: # loop will run continuosly, to stop ctrl+c
#     Easwer(10,28)
#---------------------------------------------------------------
# def dynamic_ip(name):
#     print("Hi ",name,", How r u")
# n=input("Enter the name : ")
# dynamic_ip(n)
# # #---------------------------------------------------------------
# # # *arbitrary arguments is used to pass the multiple values
# # # default it will take the values in the form of tuple"""
# def arbitrary(*data): 
#     print("Hii",data)  
#     print("Hello", list(data)) # converting tuple to list
# arbitrary(10,2,92,28,10,96) 
# #---------------------------------------------------------------
# # **kwargs is used to pass the multiple values, 
# # it will take the values in the form of dictionary
# def keyword_args(**name): 
#     print("Hii",name)
# keyword_args(name="Ram",age=25)
#---------------------------------------------------------------
def list_f(name):
    print("hii",name)
list_f([1,2,3,4,4]) # passing the list as an argument
#---------------------------------------------------------------
def outer_function():
    print("this is outer function")
    def inner_function():
        print("this is inner function")
    inner_function()
outer_function()
#---------------------------------------------------------------
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
print(add(1,2), sub(4,3), mul(2,3))