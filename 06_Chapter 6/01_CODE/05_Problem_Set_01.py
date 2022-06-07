num1 = int (input ("Enter the Number 1 : "))
num2 = int (input ("Enter the Number 2 : "))
num3 = int (input ("Enter the Number 3 : "))
num4 = int (input ("Enter the Number 4 : "))

if (num1 > num2):
    f1 = num1
else :
    f1 = num2

if (num3 > num4):
    f2 = num3
else : 
    f2 = num4

if (f1 > f2):
    print ("The greatest value is : ", f1)
else : 
    print ("The greatest value is : ", f2)
