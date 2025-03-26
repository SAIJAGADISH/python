# file=open("demo.txt",mode="r")
# # rl=file.readline()
# rls=file.readlines()
# # r=file.read()

# # print(rl)
# print(rls)
# # print(r)
# file.close()


# file=open("demo.txt",mode="a") # w mode will delete the data, so use append to add the data to existing one
# c=file.write("  this is my append mode ") # writing the data using append mode
# file.close()



# # Reading file in ‘r+’ mode:
# with open('demo.txt','r+') as fd:
#     print(fd.tell())
#     print(fd.read())
#     print(fd.tell())



##Reading file in ‘w+’ mode
with open('demo.txt','w+') as fd:
    print(fd.tell())
    print(fd.read())
    c=fd.write("this is jaga")

    print(fd.tell())
  


# Write file in ‘r+’ mode
# with open('demo.txt','r+') as fd:
#     fd.write("New text.")



# Write file in ‘w+’ mode
# with open('demo.txt','w+') as fd:
#     fd.write("New text.")



# with open('sample1.txt','r+') as fd:
#     pass

#Opening file in ‘w+’ mode when it does not exist
# with open('sample1.txt','w+') as fd:
#     pass
    


'''
tell() method can be used to get the position of File Handle. 
tell() method returns current position of file object.
This method takes no parameters and returns an integer value. 
'''


# Python program to demonstrate
# tell() method


# Open the file in read mode
# fp = open('file_error/demo.txt', "r")

# # Print the position of handle
# print(fp.tell())

# #Closing file
# fp.close()





# # Python program to demonstrate
# # tell() method

# Opening file
# fp = open('demo.txt', "r")
# fp.read(8)

# # Print the position of handle
# print(fp.tell())

# # Closing file
# fp.close()


'''
seek() function is used to change the position of the File Handle to a given specific position. 
File handle is like a cursor, which defines from where the data has to be read or written in the file. 
'''

'''
f.seek(0)	
Move file pointer to the beginning of a File
'''





# # # Opening file
# fp = open('demo.txt', "r")
# print(fp.tell())
# fp.read(2)

# # # # Print the position of handle
# print(fp.tell())  
# fp.seek(0)
# print(fp.tell())  

# # # # Closing file
# fp.close()

 

# file=open('demo.txt',mode='r+') # open
# content=file.read() # operation
# v=str(content)
# print(v)
# f=v.split()
# print(f)
# f.insert(2,'chetan')
# print(file.tell())
# file.close()
# file=open('demo.txt',mode='w')
# print(f)
# for i in f:
#     file.writelines([i])
