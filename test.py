print("This is Codelagos Trivia Quiz")
print("Select the letter with the correct answer")
score = 0
Question1 = input("(1) How many out of school centers does codelagos have? \n(a)4 \n(b)12 \n(c)21 \n(d)30\n")
if (Question1.lower()=="c"):
    print("correct")
    score = score+1
else:
    print("incorrect")
    
Question2 = input("In what year did CodeLagos start? \n(a)2017 \n(b)2012 \n(c)1999 \n(d)2018 \n")
if (Question2.lower()=="a"):
    print("correct")
    score = score+1
else:
    print("wrong")
    
Question3 = input("How many lagosian does codelagos intend to train by 2020? \n(a)1,000,000 \n(b)2,000,000 \n(c)3,000,000 \n(d) 4,000,000 \n")
if (Question3.lower()=="a"):
    print("correct")
    score = score+1
else:
    print("wrong")
