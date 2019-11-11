#Welcome to the BMI calculator
print("Welcome to the BMI calculator")
print("Please enter your weight in kilograms and your height in metres")
weight=float(input("Please enter your weight:"))
height=float(input("Please enter your height:"))
bmi=weight/(height*height)
bmi=round(bmi,1)
#Display the BMI
print("your bmi is:",bmi)
#Evaluate the bmi and give a verdict
if(bmi<18.5):
    print("Underweight")
elif((bmi>18.5)and (bmi<25)):
    print("Normal")
elif((bmi>=25)and (bmi<30)):
    print("Overweight")
else:
    print("Obese")
