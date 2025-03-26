# Remove the particular element and creating a new list
# str1 =[10,6,6,6,2,6,6,6,92,6,6,6,6,28,10,6,6,96] 
# n=[] 
# for i in str1:      # some elements are skipping !!!( we might loose data here)
#     if i==6:
#         str1.remove(6)
#     else:
#         n.append(i)
# print(n)
# print("----------------------***---------------------------")
# ##-------------------------------------------------
# # List comprehension is best way to get correct data without loosing
# str1 = [10,6,6,6,2,6,6,6,92,6,6,6,6,28,10,6,6,96]
# n = [i for i in str1 if i != 6]  # Filter out 6s
# print(n)  

####-------------------------------------------------

# #Regular way to find EVEN & ODD NUMBERS and keep it in Seperate List
# n=10
# e=[]
# o=[]
# for i in range(n+1):
#     if i%2==0:
#         E=f"{i} is even"  
#         e.append(E)     
#     else:
#         O=f"{i} is odd"
#         o.append(O)
# print(e)
# print(o)
# print("------------**-----------**---------------")
# ####-------------------------------------------------
# # #USING Short Hand IF-else
# n=10
# list = [f"{i} is EVEN" if i % 2 == 0 else f"{i} is odd" for i in range(n+1)]
# print(list)

####-------------------------------------------------

# using (in) keyword to find particular thing in elements
# newlist = []
# for x in ["apple", "banana", "cherry", "kiwi", "mango","papaya"]:
#   if "a" in x:     # -> in keyword
#     newlist.append(x)
# print(newlist)
# ####-------------------------------------------------
# fruits = ["apple", "banana", "papaya","cherry", "kiwi", "mango"]
# #new_list = [expression for item in iterable if condition]->list comprehension syntax
# newlist = [x for x in fruits if "a" in x]
# print(newlist)
####-------------------------------------------------



# To find the index of particular element in a list 
# s=[10,2,3,4,3,4]
# for i in range(len(s)):
#     if s[i]==3:
#         print(i)