greeting = "Good Morning, "
name = "Rabbit"
# Concatenating two strings
c = greeting + name
print (c)

name = "Rabbit"
print(name[4])
# name[3] = "d" --> Does not work

# Slicing of string
print(name[1:4])
print(name[:4]) # is same as name[0:4]
print(name[1:]) # is same as name[1:6]
c = name[-4:-1] # is same is name[1:4]
print(c)

name = "RabbitIsGood"
d = name[0::2]
# d = name[:0:-1]
print(d)