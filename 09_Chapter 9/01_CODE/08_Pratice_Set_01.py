f = open ('09_Poems.txt')
data = f.read()

if 'Twinkle' in data :
    print ("Twinkle is present")
else :
    print ("Twinkle is not present")
    
f.close()
