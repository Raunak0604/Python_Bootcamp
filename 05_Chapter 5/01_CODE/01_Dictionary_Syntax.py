myDict = {
    "Fast" : "In a Quick Manner",
    "Rabbit" : "a Bad boy",
    "Mark" : [32, 43, 45, 90],
    10 : 200,
    "anotherDict" : { "Rabbit" : "A coder"},
}

print (myDict["Fast"])
print (myDict["Rabbit"])
print (myDict[10])


print (myDict["Mark"])
myDict["Mark"] =[90, 76, 88]
print (myDict["Mark"])

print (myDict ["anotherDict"])
print (myDict ["anotherDict"] ["Rabbit"])