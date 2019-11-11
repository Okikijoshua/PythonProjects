print("This is an Automated Teller Machine(ATM) Simulation")
print("Insert your atm card")
print("Verifying the card")
print("################################")
print("Please Enter pin")
pin=input("Please enter pin \n")
checkpin=len(pin)
if(checkpin <4 or checkpin >4):
    print("Invalid pin")
