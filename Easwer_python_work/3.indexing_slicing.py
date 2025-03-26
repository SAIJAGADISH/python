easwer=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # method 1
esj=list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) # method 2
print(easwer[9])
print(esj[-11])     # Reverse Indexing
easwer[1]="Jagadish"   # changing Index[1] data,here 2 in index[1] and it's replaced
# slicing [start:stop:skip]
print(easwer[0:6])  # index starts with(0) -> here (0-5)
print(esj[:6])      # from begining to till 6(index means n-1= 6-1=5)
print(easwer[4:])   # from index 4 to end
print(esj[:])       # getting all data
print(easwer[6:6])  # empty list
print(esj[0:18:2])  # skip 
print(easwer[::2])  # getting all data by skipping
print(esj[::-1])    # Reverse
print(easwer[::-3]) # Reverse data and skip