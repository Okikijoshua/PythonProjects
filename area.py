""" Create a simple area calculator program that will display a list of shapes and ask the user to pick a shape they want the area calculated for. Once the user enters a
number for a shape, the other parameters for the shape are asked for and the area of the shape is displayed."""

item = int(input("This program is used to calculate area of shapes. Kindly select a shape by it number on the list. \n1. Area of a circle \n2. Area of a rectangle \n3. Area of a square \n4. Area of a triangle \n5. Area of a parallelogram\n6. Area of a Trapeziod \n"))
if(item == 1):
    shape = "area of a circle"
    radius = float(input("You wish to calculate area of a circle with formula 'πr2' \n Enter the radius \n"))
    pie = 3.142
    area = round(pie * radius,1)
    
elif(item == 2):
    shape = "area of a rectangle"
    base = float(input("You wish to calculate area of a rectangle with formula 'Base × Height' \nEnter the Base \n"))
    height =float(input("Enter the Height \n"))
    area = round(base * height,1)

elif(item == 3):
    shape = "area of a square"
    base = float(input("You wish to calculate area of a square with formula 'Base × Height' \nEnter the Base \n"))
    height =float(input("Enter the Height \n"))
    area = round(base * height,1)

elif(item == 4):
    shape = "area of a triangle"
    base = float(input("You wish to calculate area of a triangle with formula '½(Base × Height)' \nEnter the Base \n"))
    height =float(input("Enter the Height \n"))
    area = round(0.5(base * height),1)

elif(item == 5):
    shape = "area of a parallelogram"
    base = float(input("You wish to calculate area of a parallelogram with formula 'Base × Height' \nEnter the Base \n"))
    height =float(input("Enter the Height \n"))
    area = round(base * height,1)

elif(item == 6):
    shape = "area of a trapezoid"
    base1 = float(input("You wish to calculate area of a trapezoid with formula '½(Base1 + Base2) × Height' \nEnter the Base 1 \n"))
    base2 =float(input("Enter the Base 2 \n"))
    height =float(input("Enter the Height \n"))
    area = round(0.5 (base1 + base2) * height,1)

else:
    print("Invalid Option")
    
print("I have calculated the ",shape," and the area is: ",area)
