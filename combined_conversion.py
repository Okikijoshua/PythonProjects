menu = int(input("Pleasw select options of your choice \n Option(1) \n Option(2)"))
if menu ==1:
    print("sea food")
elif menu ==2:
    print("Swallow with vegetable")
else:
    print("invalid input")
    
print("This is a Conversion from Naira to any currency")
currency=int(input("Select the currency to convert to. \n1) United states Dollar $ \n2) Austrailian Dollar $ \n3) Canadian Dollar $ \n4) Pound Sterling  \n5) Euro € \n6) Chinese Yuan \n7) Japanese Yen \n8) Swiss Franc \n9) South African Rand \n10 Ghanaian Cedi\n"))
if(currency==1):
    naira=float(input("You wish to convert from Naira to United State Dollar($) \n Enter the Naira here:\n"))
    usa=0.0027
    conversion_usa= (naira * usa)
    print(conversion_usa)
    
elif(currency==2):
    naira=float(input("You wish to convert to the Austrialian Dollar\n Enter The Naira here:\n"))
    aus=0.0037
    conversion_aus=(naira * aus)
    print(conversion_aus)
    
elif(currency==3):
    naira=float(input("You wish to convert to the Canadian Dollar\n Enter The Naira here:\n"))
    canada=0.0036
    conversion_can=(naira*canada)
    print(conversion_can)  
    
elif(currency==4):
    naira=float(input("You wish to convert to the Pound Sterling\n Enter The Naira here:\n"))
    pound=0.0022
    conversion_pound=(naira*pound)
    print(conversion_pound)
    
elif(currency==5):
    naira=float(input("You wish to convert to the Euro\n Enter The Naira here:\n"))
    euro=0.0024
    conversion_euro=(naira*euro)
    print(conversion_euro)

elif(currency==6):
    naira=float(input("You wish to convert to the Chinese Yuan\n Enter The Naira here:\n"))
    yuan=0.019
    conversion_yuan=(naira*yuan)
    print(conversion_yuan)

elif(currency==7):
    naira=float(input("You wish to convert to the Japanese Yen\n Enter The Naira here:\n"))
    yen=0.31
    conversion_yen=(naira*yen)
    print(conversion_yen)

elif(currency==8):
    naira=float(input("You wish to convert to the Swiss Franc\n Enter The Naira here:\n"))
    franc=0.0028
    conversion_franc=(naira*franc)
    print(conversion_franc)

elif(currency==9):
    naira=float(input("You wish to convert to the South African Rand\n Enter The Naira here:\n"))
    rand=0.038
    conversion_rand=(naira*rand)
    print(conversion_rand)

elif(currency==10):
    naira=float(input("You wish to convert to the Ghanaian Cedi\n Enter The Naira here:\n"))
    cedi=0.013
    conversion_cedi=(naira*cedi)
    print(conversion_cedi)
    
else:
    print("Invalid Input")

