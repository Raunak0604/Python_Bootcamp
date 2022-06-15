word = {
    "pankha" : "fan",
    "vastu" : "item",
    "karenge" : "doing"
}
print (" Choose one word of these : ", word.keys())

myWord = input ("Enter a hindi word : ")
print ( " English meaning is : ", word.get(myWord))