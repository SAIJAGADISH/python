from datetime import datetime

name=input("Enter your name: ")

lists= """
Rice    Rs.20/kg
Sugar   Rs.40/kg
Salt    Rs.10/kg
oil     Rs.100/ltr
potato  Rs.30/kg
Milk    Rs.50/ltr
Ghee    Rs.200/ltr
Flour   Rs.25/kg
Biscuit Rs.10/pack
"""
price=0
totalprice=0
finalprice=0
pricelist=[]
ilist=[]
qlist=[]
plist=[]

#Rates of items

itemsList= { "RICE":20, "SUGAR":40, "SALT":10, "OIL":100, "POTATO":30,
         "MILK":50, "GHEE":200, "FLOUR":25, "BISCUIT":10, "BREAD":15}
option=int(input("For list of items - press 1:, Purchase items - press 2: "))
if option==1:
    print(lists)
while True:
    item_input = input("Enter item name (or) Enter FINISH to end): ").strip().upper()
    if item_input == "FINISH":
        break
    if item_input in itemsList:
        quantity=int(input("Enter the quantity: "))
        if item_input in itemsList.keys():
            price=quantity*itemsList[item_input]
            pricelist.append((item_input,quantity,price))
            totalprice+=price
            ilist.append(item_input)
            qlist.append(quantity)
            plist.append(price)
            gst=totalprice*0.05
            finalamount=totalprice+gst
        else:
            print("Sorry, Item is not available")
    else:
        print("Invalid input")
inp=input("can i bill the items? press 1 for yes: ")
if inp=='1':
    pass
    if finalamount!=0:
        print(40*"*", "Easwer's Super Market", 40*"*")
        print(42*"-", "Hanuman junction", 37*"-")
        print(90*"-")
        print("Name: ", name,25*" ", "Date: ", datetime.now())
        print(90*"-")
        print("{:<15} {:<20} {:<1}".format("Item_name", "Quantity", "Price"))
        print(90*"-")
        for i in range(len(pricelist)):
            print("{:<18} {:<20} {:<1}".format(ilist[i], qlist[i], plist[i]))
        print(90*"-")
        print(20*" ", "Total Price: ", 'Rs',totalprice)
        print(20*" ", "   GST:      ", 'Rs',gst)
        print(90*"-")
        print(20*" ", "Final Price: ", 'Rs',finalamount)
        print(90*"-")
        print(50*"-", "Thank you for shopping with us", 50*"-")
    print(60*"=", "Visit Again", 60*"=")
else:
    print("Thank you for shopping with us")
    print("Visit Again")

    