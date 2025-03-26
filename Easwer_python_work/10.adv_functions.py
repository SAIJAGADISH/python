'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments,
but can only have one expression.
syntax->  lambda arguments : expression
'''
# x = lambda a,b,c : a + b + c
# print(x(10,2,92))
# ##---------------------------
# l1=[10,2,92] # list
# l2=[28,10,96] # list
# l3=[1,19,10]	#list
# l4=[]#empty list
# for i,j,k in zip(l1,l2,l3): 
#     t=lambda a,b,c : a*b+c  #
#     l4.append(t(i,j,k))
# print(l4)
#--------------------------------------------------------------
# # Regular Function
# def square(i):
#     return i * i
# i=int(input("Enter the value to square:"))
# print(square(i))  

# # Lambda Function
# e=int(input("Enter the value to square:"))
# square = lambda e: e * e
# print(square(e))  

# # lambda inside multiplier which is assign to double. Now, double stores lambda function
# def multiplier(n):
#     return lambda x: x * n  # returns -> lambda x: x * 2 

# double = multiplier(2) # Means-> double = lambda x: x * 2
# print(double(5))
#--------------------------------------------------------------
''' FILTER FUNCTION
The filter() method filters the given sequence with the help of a function 
that tests each element in the sequence to be true or not. It gives true elements as output.

syntax: filter(function, sequence)

Parameters:
function: function that tests if each element of a sequence true or not.
sequence: which needs to be filtered,it can be sets,lists,tuples,or containers of any iterators.
Returns:returns an iterator that is already filtered.
'''
# ages = [10,28,33,44,55]

# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True

# adults = filter(myFunc, ages)
# print(tuple(adults))

#------
#List of products represented as dictionaries.
# products = [
#     {"name": "Laptop", "price": 1200, "stock": 10},
#     {"name": "Mouse", "price": 20, "stock": 0},
#     {"name": "Keyboard", "price": 50, "stock": 5},
#     {"name": "Monitor", "price": 200, "stock": 0},
#     {"name": "Smartphone", "price": 800, "stock": 15},
# ]
# # Define a predicate function that returns True for products in stock.
# def is_available(product):
#     return product["stock"] > 0
# # Use filter() to select products that are in stock.
# available_products = list(filter(is_available, products))
# print(available_products)
# # Display the available products with formatted output.
# print("Available Products:")
# for product in available_products:
#     print(f"{product['name']:<15}Price: ${product['price']:<10} Stock: {product['stock']}")

#--------------------------------------------------------------

''' MAP FUNCTION    -> map(function, iterables)  
The python map() function is used to return a list of MODIFIED results
after applying a given function to each item of an iterable(list, tuple etc.)'''
# def calculateAddition(n):
#     return n+n    
# numbers = (1, 2, 3, 4)  
# result = map(calculateAddition, numbers)  
# print(list(result))

# #REAL TIME DISCOUNT SCENARIO USING MAP FUNCTION.  List of product prices
# prices = [100, 150, 200, 50, 75]
# def apply_discount(price):
#     discount_rate = 0.9  # 10% discount means you pay 90% of the price.
#     return round(price * discount_rate, 2)  # round to 2 decimal places

# # Use map() to apply the discount to each price in the list.
# discounted_prices = list(map(apply_discount, prices))
# print("Original Prices: ", prices)
# print("Discounted Prices:", discounted_prices)


#--------------------------------------------------------------


'''reduce() function, Syntax -> reduce(function,sequence)
 as the name describes, applies a given function to the iterables and returns a single value.'''

# from functools import reduce # from functools module , importing reduce function
# d=reduce(lambda a,b:(a+b)*2,[23,21,45,98])
# #[(23+21)*2=88(a),b(45)],[(88+45)*2=266(a),b(98)],[(266+98)*2=728]
# print("Reduce Test:",d)

# #---- REAL TIME REDUCE SCENARIO
# from functools import reduce
# #A list of transactions,where each transaction is a dictionary containing price and quantity.
# transactions = [
#     {"price": 20, "quantity": 2},   # Revenue = 20 * 2 = 40
#     {"price": 15, "quantity": 1},   # Revenue = 15 * 1 = 15
#     {"price": 30, "quantity": 3},   # Revenue = 30 * 3 = 90
#     {"price": 10, "quantity": 5}    # Revenue = 10 * 5 = 50
# ]
# #reduce() takes each element from transactions one by one and applies the lambda function.
# #The current element (dictionary) is assigned to txn.'acc' is accumalator,initially it is 0 at end
# total_revenue = reduce(lambda acc, txn: acc + txn["price"] * txn["quantity"],transactions,0)                   
# print("Total Revenue: Rs.", total_revenue)

#-----------------------------------------

'''
Generator-Function : A generator-function is defined like a normal function,
but whenever it needs to generate a value, it does so with the yield keyword rather than return.
If the body of a def contains yield, the function automatically becomes a generator function.'''
# A Python program to demonstrate use of generator object with next()
# def simpleGeneratorFun():
# 	yield 1
# 	yield 2
# 	yield 3

# # x is a generator object
# x = simpleGeneratorFun()

# # Iterating over the generator object using next
# print(x.__next__()) # In Python 3, __next__()
# print(x.__next__())
# #print(x.__next__())
'''
The yield statement is responsible for controlling the flow of the generator function.
It pauses the function execution by saving all states and yielded to the caller. 
Later it resumes execution when a successive function is called. 
We can use the multiple yield statement in the generator function.

The return statement returns a value and terminates the whole function 
and only one return statement can be used in the function.
'''
# def aa():
#     yield 1+1
#     yield 2+1
# x=aa()
# print(x.__next__())#__next__() is used to manually get the next value from an iterator
# print(x.__next__())#commonly used when working with generators and iterators.
# print("------*------*------")
# #----------------
# def bb():
#     return 1+1
#     return 2+1
# x=bb()
# print(x)

##------------------------------------------------------------------------------

# def add(*a):
#     return sum(a+a) # if we give a+a without using sum, then it will concatinate
# b=add(1,2,3,4,5,67,8,5)
# print(b)
# ##----------------------------------------------------------------------------------------------------------------------------
# def add(a,b):
#     return a+b
# print(add(1,2))
##-------------------------------------------------------------------------------
# def Easwer(a,b):
#     print(a*b*a*b*a)
# Easwer(1,2)
##-------------------------------------------------------------------------------
#lambda testing
# a="Jaga"
# b="dish "
# c=" * "

# s=lambda j,d,c:((j+d)+c)*5
# print(s(a,b,c),"\n")

# esj=lambda e,s,j:[e+s+j]*2
# print(esj("Easwer ","sai ","jagadish"))
#--------------------------------------------------------------

# Normal function to get even numbers
# def even(number):
#     even_num=[]
#     for x in number:
#         if x%2==0:
#             even_num.append(x)
#     print(even_num)
# even([10,28,92,96,111,211,233])
# #--------------------------------------------------------------
# # #diff bw filter and map

# # using filter to get even numbers using one line lambda
# nums = [10,28,92,96,111,211,233]
# filter = list(filter(lambda x: x%2==0, nums))#based on condition filter accepts TRUE only
# print(tuple(filter)) # saving final result as filter object,saved it into tuple/list---

# map = list(map(lambda x: x**2, nums))#based on expression map modifies the data
# print(list(map)) #here we saved in list