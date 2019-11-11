print("This is a conversion to Naira")
currency1=int(input("Selesct the currency from which to convert. \n1) United states Dollar $ \n2) Austrailian Dollar $ \n3) Canadian Dollar $ \n4) Pound Sterling  \n5) Euro € \n6) Chinese Yuan \n7) Japanese Yen \n8) Swiss Franc \n9) South African Rand \n10 Ghanaian Cedi\n"))
if(currency1==1):
    naira_1=float(input("You wish to convert from US Dollar to Naira \nEnter the Amount Here\n"))
    usa_1=362.08
    conversion_usa_1= (naira_1*usa_1)
    print(conversion_usa_1)
    
elif(currency1==2):
    naira_1=float(input("You wish to convert from Austrailian Dollar to Naira \nEnter the Amount Here\n"))
    aus_1=262.96
    conversion_aus_1= (naira_1*aus_1)
    print(conversion_aus_1)
    
elif(currency1==3):
    naira_1=float(input("You wish to convert from Canadian Dollar to Naira \nEnter the Amount Here\n"))
    canada_1=273.95
    conversion_canada_1= (naira_1*canada_1)
    print(conversion_canada_1)
    
elif(currency1==4):
    naira_1=float(input("You wish to convert from Pound Sterling to Naira \nEnter the Amount Here\n"))
    pound_1=464.49
    conversion_pound_1= (naira_1*pound_1)
    print(conversion_pound_1)
    
elif(currency1==5):
    naira_1=float(input("You wish to convert from Euro to Naira \nEnter the Amount Here\n"))
    euro_1=416.53
    conversion_euro_1= (naira_1*euro_1)
    print(conversion_euro_1)
    
elif(currency1==6):
    naira_1=float(input("You wish to convert from Chinese Yuan to Naira \nEnter the Amount Here\n"))
    yuan_1=52.88
    conversion_yuan_1= (naira_1*yuan_1)
    print(conversion_yuan_1)
    
elif(currency1==7):
    naira_1=float(input("You wish to convert from Japanese Yen to Naira \nEnter the Amount Here\n"))
    yen_1=3.24
    conversion_yen_1= (naira_1*yen_1)
    print(conversion_yen_1)
    
elif(currency1==8):
    naira_1=float(input("You wish to convert from Swiss Franc to Naira \nEnter the Amount Here\n"))
    franc_1=366.33
    conversion_franc_1= (naira_1*franc_1)
    print(conversion_franc_1)
    
elif(currency1==9):
    naira_1=float(input("You wish to convert from South African Rand to Naira \nEnter the Amount Here\n"))
    rand_1=25.79
    conversion_rand_1= (naira_1*rand_1)
    print(conversion_rand_1)
    
elif(currency1==10):
    naira_1=float(input("You wish to convert from Ghanaian Cedi to Naira \nEnter the Amount Here\n"))
    cedi_1=73.15
    conversion_cedi_1= (naira_1*cedi_1)
    print(conversion_cedi_1)

else:
    print("Invalid Input")
     
