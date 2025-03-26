# Tuple is a collection of elements which is ordered and (immutable)unchangeable.
# Tuple allows duplicate members.

# ESJ=(1,2,3,4,5,6,7,8,9,10)
# print(ESJ[0])       # output 1
# ##ESJ[0]=10 #TypeError: 'tuple' object does not support item assignment
# print(ESJ)

# #tuple operations

# Easwer=(10,2,92,28,10,96)
# print(Easwer)       # output: (10, 2, 92, 28, 10, 96)
# print(max(Easwer)) # output: 96
# print(min(Easwer)) # output: 2
# print(sum(Easwer)) # output: 238
# print(len(Easwer)) # output: 6
# print(list(Easwer)) # output: [10, 2, 92, 28, 10, 96]
# print(tuple(Easwer)) # output: (10, 2, 92, 28, 10, 96)
# ##-------------------------------------
#INDEXING
# my_tuple = ('p','e','r','m','i','t')
# print(my_tuple.index('p')) # Output -> 0
# print(my_tuple[0]) # Output -> 'p'
# print(my_tuple[5]) # Output -> 't'
# #-------------------------------------
# #NEGATIVE INDEXING
# my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
# print(my_tuple[-1]) # Output -> 't'
# print(my_tuple[-6]) # Output -> 'p'
# #-------------------------------------
# # # Nested index
# n_tuple = ("India", [10,2,92], (28,10,96))
# print(n_tuple[0][3]) # Output ->  i
# print(n_tuple[1][1]) # Output ->  2
# print(n_tuple[2][2]) # Output -> 96
#-------------------------------------

# #slicing
# my_tuple = ('p','r','o','g','r','a','m','i','n','g')
# print(my_tuple[1:4]) # ('r', 'o', 'g')
# print(my_tuple[:-6]) # ('p', 'r', 'o', 'g')
# print(my_tuple[7:]) # ('i', 'n', 'g')
# print(my_tuple[:]) # ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'n','g')
# #-------------------------------------
# # Changing a Tuple.
# # Tuple is immutable(unchangeable),
# # But we can change the values of the tuple elements which are in list
# my_tuple = (4, 2, 3, [6, 5])
# my_tuple[3][0] = 9 # Output: (4, 2, 3, [9, 5])
# print(my_tuple)
#-------------------------------------
# Membership operators  in and not in
# d=(2,3,4,5,6,6,10,7,7,87,88,8)
# print(10 in d)      #output: True
# print(22 not in d)  #output: True
# #-------------------------------------
# #Identity operators is and is not
# t1=(1,2,3)
# t2=(1,2,3)
# t3=t1
# # Don’t depend on 'is' for immutable objects like tuples,integers, or strings
# # Python sometimes reuses memory (but not always).
# print(t1 is t2) #Ture or False
# print(t1 is t3) #True, t3 is referring to the same object as t1

# print(t1==t2) #True     Always use == for content comparison.

# t1=(1,2,3)
# t2=(1,2,3,10,28)
# print(t1 is not t2) #True
#-------------------------------------

# d=(10,28)
# print(d*5) #(10, 28, 10, 28, 10, 28, 10, 28, 10, 28)
# a="Ram "
# print(a*10) # Ram Ram Ram Ram Ram Ram Ram Ram Ram Ram 
# #-------------------------------------
# t1=(1,2,3)
# t2=(4,5,6)
# print(t1+t2) #concatenates the two tuples
# new=[]
# for i,j in zip(t1,t2): #zip() function is used to combine two tuples
#     print((i,j),end=" ")
#     new.append(i+j) #adds the elements of the two tuples
# print(tuple(new)) 
#-------------------------------------
# my_tuple = ()
# print(my_tuple) # Output: ()
# my_tuple = (1, 2, 3)
# print(my_tuple) # Output: (1, 2, 3)
# my_tuple = (1, "Hello", 3.4)
# print(my_tuple) # Output: (1, "Hello", 3.4)
# my_tuple = ("India", [10,2,92], (28,10,96))
# print(my_tuple) # Output: ("India", [10,2,92], (28,10,96))
#-------------------------------------
# d=(1,2,3,35,4,6,7,8)
# for i in d:
#     print(i) 