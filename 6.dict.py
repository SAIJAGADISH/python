# Student={"sno":1,"name":"Easwer","phone":[94943,14945], 10:True}
# print(Student)
# print(Student.get("sno")) # get method is used to get the value of the key
# print(Student.keys()) # keys method is used to get the keys of the dictionary
# print(Student.values()) # values method is used to get the values of the dictionary
# print(Student.items()) #items method is used to get items of the dictionary in the form of tuple
# Student.update({"name":"Indh"}) # update method is used to update the value of the key
# print(Student)
# Student.pop(10) # pop method is used to remove the key and value from the dictionary
# print(Student)
# #Student.pop() # need to give mandatory argument
# print(list(Student)) #list is used to get the keys of the dictionary in the form of list
# ESJ=Student.copy() # copy method is used to copy the dictionary
# Student.clear() # clear method is used to clear the dictionary
# print(Student)
# print(ESJ)
# ESJ.popitem()#popitem method is used to remove the last key and value from the dictionary
# print(ESJ)
# del ESJ # del is used to delete the dictionary
# print(ESJ) # NameError: name 'ESJ' is not defined
##--------------------------------

# esj={"sno":1,"name":"Easwer","phone":[12,32]}
# for a,b in esj.items():
#     print(a,b)
# for a in esj:
#     print(a,esj.get(a))


# phani={
#     1:"a",
#     2:"b",
#     3:{1:"aa"},
# }
# print(phani[3][1])

r=dict()
print(r)
r = dict(name="Ram", age=108, city="Ayodhya")
print(r)
