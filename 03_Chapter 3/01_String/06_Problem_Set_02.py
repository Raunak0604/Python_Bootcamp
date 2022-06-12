letter = '''Dear <|Name|>
\tYou are selected !
Date : <|Date|>'''

name = input ("Enter your name : \n")
date = input ("Enter date : \n")

letter = letter.replace ("<|Name|>" ,name)
letter = letter.replace ("<|Date|>" ,date)

print (letter)