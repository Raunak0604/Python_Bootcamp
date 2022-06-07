# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

def sum (n) :
    if n <= 1 :
        return n
    return sum (n-1) + n

p = sum (5)
print(p)