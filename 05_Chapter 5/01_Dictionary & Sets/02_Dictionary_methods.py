myDict = {
    "Fast" : "In a Quick Manner",
    "Rabbit" : "a Bad boy",
    "Mark" : [32, 43, 45, 90],
    10 : 200,
    "anotherDict" : { "Rabbit" : "A coder"},
}

# Dictionary Methods
print(myDict.keys()) # Prints the keys of the dictionary
print(type(myDict.keys())) # type
print(list(myDict.keys())) # type casting 
print(myDict.values()) # Prints the value of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "souvik": "Friend",
    "yashwant": "Friend",
    "samboron": "Friend",
    "Rabbit": "A Dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("Rabbit")) # Prints value associated with key "harry"
print(myDict["Rabbit"]) # Prints value associated with key "harry"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("Rabbit2")) # Returns None as harry2 is not present in the dictionary
# print(myDict["Rabbit2"]) # throws an error as harry2 is not present in the dictionary