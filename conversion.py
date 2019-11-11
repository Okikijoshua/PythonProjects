#Omikune Okiki Joshua
#okikiomikunl@gmail.com
# +2348188737690,


print("This is a Currency Converter Platform")
choice = int(input("Choice any of this: \n1) From Naira to any currency \n2) From any currency to Naira \n"))
if choice == 1:
    print("This is a Conversion from Naira to any Currency")
    currency=int(input("Select the currency to convert to. \n1) United states Dollar $ \n2) Austrailian Dollar $ \n3) Canadian Dollar $ \n4) Pound Sterling  \n5) Euro € \n6) Chinese Yuan \n7) Japanese Yen \n8) Swiss Franc \n9) South African Rand \n10) Ghanaian Cedi\n"))
    if(currency==1):
        naira=float(input("You wish to convert from Naira to United State Dollar($) \n Enter the Naira here:\n"))
        usa=0.0027
        conversion_usa= (naira * usa)
        print("The current rate of",naira,"is",conversion_usa)
    
    elif(currency==2):
        naira=float(input("You wish to convert to the Austrialian Dollar\n Enter The Naira here:\n"))
        aus=0.0037
        conversion_aus=(naira * aus)
        print("The current rate of",naira,"is",conversion_aus)
    
    elif(currency==3):
        naira=float(input("You wish to convert to the Canadian Dollar\n Enter The Naira here:\n"))
        canada=0.0036
        conversion_can=(naira*canada)
        print("The current rate of",naira,"is",conversion_can)  
    
    elif(currency==4):
        naira=float(input("You wish to convert to the Pound Sterling\n Enter The Naira here:\n"))
        pound=0.0022
        conversion_pound=(naira*pound)
        print("The current rate of",naira,"is",conversion_pound)
    
    elif(currency==5):
        naira=float(input("You wish to convert to the Euro\n Enter The Naira here:\n"))
        euro=0.0024
        conversion_euro=(naira*euro)
        print("The current rate of",naira,"is",conversion_euro)

    elif(currency==6):
        naira=float(input("You wish to convert to the Chinese Yuan\n Enter The Naira here:\n"))
        yuan=0.019
        conversion_yuan=(naira*yuan)
        print("The current rate of",naira,"is",conversion_yuan)

    elif(currency==7):
        naira=float(input("You wish to convert to the Japanese Yen\n Enter The Naira here:\n"))
        yen=0.31
        conversion_yen=(naira*yen)
        print("The current rate of",naira,"is",conversion_yen)

    elif(currency==8):
        naira=float(input("You wish to convert to the Swiss Franc\n Enter The Naira here:\n"))
        franc=0.0028
        conversion_franc=(naira*franc)
        print("The current rate of",naira,"is",conversion_franc)

    elif(currency==9):
        naira=float(input("You wish to convert to the South African Rand\n Enter The Naira here:\n"))
        rand=0.038
        conversion_rand=(naira*rand)
        print("The current rate of",naira,"is",conversion_rand)

    elif(currency==10):
        naira=float(input("You wish to convert to the Ghanaian Cedi\n Enter The Naira here:\n"))
        cedi=0.013
        conversion_cedi=(naira*cedi)
        print("The current rate of",naira,"is",conversion_cedi)
    else:
        print("Invalid Input")
        
elif choice == 2:
    print("This is a Conversion from any currency to Naira")
    currency1=int(input("Select the currency from which to convert. \n1) United states Dollar $ \n2) Austrailian Dollar $ \n3) Canadian Dollar $ \n4) Pound Sterling  \n5) Euro € \n6) Chinese Yuan \n7) Japanese Yen \n8) Swiss Franc \n9) South African Rand \n10) Ghanaian Cedi\n"))
    if(currency1==1):
        naira_1=float(input("You wish to convert from US Dollar to Naira \nEnter the Amount Here\n"))
        usa_1=362.08
        conversion_usa_1= (naira_1*usa_1)
        print("The current rate of",naira_1,"is",conversion_usa_1)
    
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

else:
    print("Invalid Option")
