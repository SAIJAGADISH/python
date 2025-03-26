# ..................... " Sets " .............................
# Sets are iterable, but not sequence data type.
# sequence require order,index,and can do slicing.
# The elements in the set cannot be duplicates.
# Sets contain unique elements only and unordered.
# The elements in the set are mutable(can be modified).
# There is no index attached to any element in a python set. 
# So they do not support any indexing or slicing operation.
# We can add or remove items from it.
# defined with {}
# A set is created by placing all the(elements)inside curly braces {},
# separated by comma , or by using the built-in set() function. 
# # list() ,set() , tuple()

# sekhar={1,2,2}
# print(type(sekhar))

# shiva=set()
# print(type(shiva))
# print(sekhar,shiva)

# l=[1,1,2,3,4,4,5,65]
# s=set(l)
# l=list(s)
# t=tuple(l)
# print(s,l,t)

# #---------------------set methods---------------------
#  #Set Methods- > add , remove , pop , clear , copy , update, discard.
# Easwer={10,20,1,2,1,2,3,5,4,3,4,5,6,9,8,7,6,5,4}
# print(Easwer)
# Easwer.add(100) # Sets are unordered,added elements can be anywhere.sets have no index
# print(Easwer)
# Easwer.remove(1) # if element is not present in the set it will give error
# print(Easwer)
# Easwer.discard(11) # if element is not present in the set it will not give any error
# print(Easwer)
# Easwer.discard(13)
# print(Easwer)
# Easwer.pop() # it will remove the first element from the set 
# Easwer.pop()
# Easwer.pop()
# print(Easwer)
# Easwer.update([22,33,44,55,666,888,99,11])
# print(Easwer)
##print(Easwer.remove(1)) # if element is not present in the set it will give error

# #---------------------set operations---------------------
# Union, intersection, difference, symmetric difference

# s1={1,2,3,4,5,6,7,9,10,11}
# s2={1,2,3,4,5,6,7,8,12,13}

# print(s1.union(s2))  # all elements , here output is 1,2,3,4,5,6,7,8,9,10,11,12,13

# print(s1.intersection(s2)) # common elements , here output is 1,2,3,4,5,6,7

# print(s1.difference(s2)) # s1-s2 , here output is 9,10,11
# print(s2.difference(s1)) # s2-s1 , here output is 8,12,13

# print(s1.symmetric_difference(s2))#opposite to intersection elements,output:8,9,10,11,12,13
# print(s2.symmetric_difference(s1)) # here also output is 8,9,10,11,12,13

# issuperset, issubset, isdisjoint

s3={5,6,9,8}
s4={1,2,3,4,7}
print(s3.isdisjoint(s4))#if no common elements it will return True,else False , here output is True

e1={1,2,3,4,5}
e2={1,2,3,4,5,6,7,8,9,10}
print(e1.issubset(e2)) # subset means child ,  here output is True
print(e1.issuperset(e2)) # superset means parent,  here output is False

Easwer={1,2,1,2,3,1,3,4,3,1,2,4,(5,5,5,6,6,9),8,1+2j}
jagadish={1,2,1,2,3,1,3,4,3,1,2,4,"jagath",10.02,(5,6,9),8,1+2j}
print(Easwer, jagadish)
#---------------------------------------------------------
# for s in e1:
#     print(s)
# #---------------------------------------------------------
# s=("this {} is {}".format("book","great"))
# print(s)