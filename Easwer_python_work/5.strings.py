#strings are immutable(unchangable),trying to change a character directly results in an error.
#Memory Efficiency → Immutable objects can be shared (interning), reducing memory usage.
#Thread Safety → Since they cannot be modified, multiple threads can use the same string safely.
#Security → Prevents accidental modification, making strings safer in cryptographic and sensitive applications.
#Use replace(), slicing, join(), or concatenation to create modified versions.
###-------------------------------------------------------------------------------------------
#we must create a new string using operations like slicing, concatenation, or replace().

# # using replace()
# s = "rama"
# new_s = s.replace("r", "R")
# print(new_s)  # "Rama"

# #using concatination
# s = "rama"
# s = "R" + s[1:]  # Creating a new string
# print(s)  # "Rama"

# #using join()
# s = "rama"
# s = "".join(["R", s[1:]])  # Joining a new first letter
# print(s)  # "Rama"

###-------------------------------------------------------------------------------------------
# Easwer="ISKON's"
# Sai='Easwer'
# Jagadish='''
#  Hare Rama
#  Hare Krishna
#  Om Namah Shivaya
# '''
# print(type(Easwer),type(Sai),type(Jagadish))
# print(Easwer,Sai,'\n',Jagadish)
##----------------------------------------------------------------------------------------------
# variable.method
# EASWER="  Sri Ram Jaya Ram Jaya Jaya Ram   "
# EASWER1="Sri Ram Jaya Ram Jaya Jaya Ram"
# print(EASWER.lower())
# print(EASWER.upper())
# #---------
# print(EASWER.find("Ram"))
# print(EASWER.find("Shiv")) # find is used to control the error by giving -1
# print(EASWER.index("Jaya"))
# # #print(EASWER.index("Shiv")) # index is used to show error by giving ValueError
# ##print(EASWER.index(0))
# # #---------
# print(EASWER1.startswith("Sri"))
# print(EASWER1.endswith("RAM")) # case sensitive Ram , so it will give False
# ##---------
# print(EASWER.count("Ram")) # count() is used to count the number of times the word is repeated in the string

# #---------
EASWER="  Sri Ram Jaya Ram Jaya Jaya Ram   "
print(len(EASWER)) # len() is used to count the length of the string
s=EASWER.strip() # strip() is used to remove the spaces from the string
print(len(s))
s=EASWER.lstrip() # lstrip() is used to remove the spaces from the left side of the string
print(len(s))
s=EASWER.rstrip() # rstrip() is used to remove the spaces from the right side of the string
print(len(s))
#---------
sai="Easwer100292"
print(sai.isalpha()) # isalpha() is used to check whether the string is alphabetic or not
print(sai.isalnum()) # isalnum() is used to check whether the string is alphanumeric or not
#-----------Title()
f="bhagavad gita,hare rama hare krishna"
print(f.title()) # title() is used to capitalize the first letter of each word
print(f)
# #-----------format() ->is used to replace the {} with the given string
# names=["Ram","Sita","Lakshman","Hanuman"]
# for esj in names:
#     print("Hii {}, How r u?".format(esj)) 

# #-----------replace()
# # replace() method replaces only the first 'n' occurrences when count is specified.
# # If count is not specified, it replaces all occurrences.
# shiva="Hare Rama Hare Rama,Rama Rama"
# om=shiva.replace('Hare',"Hare Hare").replace(" Rama"," Krishna")
# print(om)
# om=shiva.replace(" Hare"," Hare hare",1) # " Hare" is 2nd one
# print(om)
# om=shiva.replace("Rama","krishna",3) # count 3 is the number of occurences to be replaced
# print(om)

##------------split(),join()
# e="This is Easwer"
# print(e)
# E=(e.split())# split() is used to split the string into list of strings
# print(E)
# j=[]
# for i in E:
#     if i=="Easwer":
#         i="Jagadish"
#         j.append(i)
#     else:
#         j.append(i)
# print(j)

# esj=" ".join(j) # join() is used to join the list of strings
# print(esj)
##----------------------------------------------------------------------------------------------

# in_websites=[]
# com_websites=[]
# for i in ["iskon.com","india.in","isha.in","gita.com","ayodhya.com"]:
#     if i.endswith("in"):
#         in_websites.append(i)
#     else:
#         com_websites.append(i)
# print(".in_websites",in_websites)
# print(com_websites)

##----------------------------------------------------------------------------------------------
"""
# #a,c are variable names. 
# #Below methods are to modify or get T/F  just by using variable.method()

a.lower(),a.upper(),a.title(),a.strip(), a.lstrip(),a.rstrip()- To modify
a.isalpha(), a.isalnum()-> T/F 
c= a.split() ,  c= " ".join(a)

##Below are the methods to find the string in the string
c= a.replace("{","").replace("}","").replace(",","\n").replace("'","")
a.count("ram")
a.startswith("SRI"), a.endswith("ram"),-> returns True or False
a.find("shiv") -> returns -1 if not found ,if found returns the index of the string
a.index("shiv") -> returns ValueError if not found ,if found returns the index of the string
('This is {} '.format(Rama)) -> output is "This is Rama" 
"""
##----------------------------------------------------------------------------------------------
## project based on using all these string methods

# def clean_message(msg):
#     """Removes extra spaces and formats the message properly."""
#     msg = msg.strip()  # Remove extra spaces from both sides
#     msg = msg.replace(" u ", " you ")  # Replace short forms
#     msg = msg.replace(" r ", " are ")
#     msg = msg.title()  # Convert to title case
#     return msg

# def analyze_chat(chat):
#     """Analyzes a chat conversation."""
#     messages = chat.split("\n")  # Split chat into messages
#     print(messages)

#     # Clean and format messages
#     cleaned_messages = [clean_message(msg) for msg in messages]
#     print(cleaned_messages)

#     # Join messages back for processing
#     chat_cleaned = " ".join(cleaned_messages)
#     print(chat_cleaned)

#     # Count occurrences of key words
#     hello_count = chat_cleaned.lower().count("hello")
#     bye_count = chat_cleaned.lower().count("bye")

#     # Check for specific words
#     has_question = chat_cleaned.endswith(" ")
#     starts_with_hi = chat_cleaned.lower().startswith("hi")

#     # Finding the first occurrence of "thank"
#     thanks_index = chat_cleaned.lower().find("thank")
    
#     # Summary Report
#     print("\n--- Chat Analysis Report ---")
#     print(f"Total Messages: {len(cleaned_messages)}")
#     print(f"'Hello' Count: {hello_count}")
#     print(f"'Bye' Count: {bye_count}")
#     print(f"Chat starts with 'Hi'? {'Yes' if starts_with_hi else 'No'}")
#     print(f"Chat ends with a question? {'Yes' if has_question else 'No'}")
    
#     if thanks_index != -1:
#         print(f"'Thank' found at index: {thanks_index}")
#     else:
#         print("'Thank' not found in chat.")

#     print("\n--- Cleaned Chat ---")
#     for i, msg in enumerate(cleaned_messages, 1): #enumerate(iterable, start=0)
#         #iterable: The list (or other iterable) to loop through.
#         #start: The starting index (default is 0, but we set it to 1 in this case).

#         print(f"{i}. {msg}")

# # Sample Chat Data
# chat_data = """
#    hi, how r u ?  
# hello! i am fine. what about u?  
# i'm good too. thanks for asking!  
# bye, see you soon.   
# """

# # Run Chat Analyzer
# analyze_chat(chat_data)
##----------------------------------------------------------------------------------------------
# strings=input("Enter the String")
# print("palindorm") if strings==strings[::-1] else print("not a palindorm")