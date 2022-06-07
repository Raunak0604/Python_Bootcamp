sub1 = int (input ("Enter the marks of subject_1 : "))
sub2 = int (input ("Enter the marks of subject_2 : "))
sub3 = int (input ("Enter the marks of subject_3 : "))

if (sub1 < 33 or sub2 < 33 or sub3 < 33) :
    print ("You are fail because you have less than 33 percent in one of the subjects")
elif (sub1 + sub2 + sub3)/3 < 40 :
    print ("You are fail due to total percentage less than 40 ")
else : 
    print ("You are pass")