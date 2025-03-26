## append,extend,insert,sort,reverse -> are only in list methods
## remove is used only in list and set methods
## clear,copy,pop -> are used in list,set and dict methods
## count,index -> are used in list,set and tuple methods

easwer=[1,2,3,4,5,6,6,7,7,8,9,10,10,10,11,12,13,14,15] # method 1
# 1.append
# easwer.append(16) #append is used to add an element in the end of the list
# print(easwer)
# easwer.append([17,18,19]) #to add multiple elements using append,it comes as sublist
# print(easwer)
# #----------------------------------------------------
# # 2.extend -use extend to overcome sublist,to add multiple elements at end of the list
# easwer.extend([20,21,22])
# print(easwer)
# #---------------------------------------------------------
# # 3.count - to count the number of times an element is repeated in the list
# print(easwer.count(10))  # 3 is output
# # #--------------------------------------------------------
# # # 4.index - to find the index of an element in the list
# print(easwer.index(10)) # to find in which index position, 10 is present
# easwer[5]=1092 # to change element using index value 
# print(easwer)
# print(easwer[8]) # to find the particular index element
#----------------------------------------------------------
# 5.clear - to clear the list
# easwer.clear()
# print(easwer)           # output is [] -> empty list
# print(easwer.clear())
# easwer.extend([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
# # #-------------------------------------------------------------
# # # 6.copy - to copy the list
# esj=easwer.copy()
# print(esj)
# easwer.extend([10,15,16,17,18,19,20,10]) #latest extend elements in easwer not copied to esj
# print(easwer)
# print(esj)
# # #---------------------------------------------------------------
# # # 7.insert - to insert an element in a particular index
# easwer.insert(1,1002) # to insert element in a particular index value 
# easwer[11]=100292 # another way to insert element in index value
# print(easwer)
# #---------------------------------------------------------------
###easwer=[1, 1002, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100292, 12, 13, 14, 10, 15, 16, 17, 18, 19, 20, 10]
# # 8. pop - to remove an element based on INDEX
# easwer.pop(1) # element inside the index 1 is popped, here 1002 is popped
# print(easwer) # in output 1002 is removed
# print(easwer.pop(4)) # to print the popped value from the list ,output 5 is removed
# print(easwer.pop()) # to remove the last element from the list
# #------------------------------------------------------------------
# ## 9.remove - removes the element from the list,1st occurence will be removed
# easwer.remove(10)
# easwer.remove(12)
# ##easwer.remove(21) -> ValueError: list.remove(x): x not in list
# print(easwer)
# #----------------------------------------------------------------
## 10.reverse - to reverse the list
###easwer=[29,32,12,3,31,5,7,43,56,33,23,2,1,6,8,53,78,9,4,3]
# easwer.reverse()
# print(easwer)
# #------------------------------------------------------------------
# ## 11.sort - to sort the list
# easwer.sort()
# print(easwer)
# #--------------------------------------------------------------------
# ## 12. reverse sort
# easwer.sort(reverse=True)
# print(easwer)
