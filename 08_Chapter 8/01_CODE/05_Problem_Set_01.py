def max (num1, num2, num3) : 
    if (num1 > num3) :
        if (num1 > num2):
            return num1
        else :
            return num3
    else :
        if (num2 > num3) :
            return num2
        else :
            return num3

p = max (123, 32, 25)
print (p)
