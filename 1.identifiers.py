""" good identifiers -> Can contain letters (A-Z, a-z), digits (0-9), and underscores (_).
easwer=1992
_easwer=10             -> Must begin with letter or __
easwer10= "dob"
easwer="easwer"
----------------------------
bad identifiers         -> shouln't use keywords (Ex: if, class, global, pass, ---)
10easwer=10021992       -> shouldn't start with number
@easwer=1
easwer#="jagadish" 
"""   
easwer=10 #int value assign to variable easwer
dob="10-02-1992" # string value assign to variable dob
ip= input("Enter the int value:") # by default dynamic input is in string format
conversion = int(ip) # using type conversion, converting string input into int
dynamic_type_conversion= float(input("Enter float value:")) #dynamically converting string format to float
explicit_tc=int(dynamic_type_conversion)#dataloss in explicit type conversion due to float to int type
implicit_tc=float(explicit_tc)# now convert int to float, we dont loose data,and get decimals with 0
print(easwer,dob)
print(conversion,dynamic_type_conversion,explicit_tc,implicit_tc)
print(type(ip),type(conversion),type(dynamic_type_conversion),type(explicit_tc),type(implicit_tc))
