def game():
    return 44677

score = game()
with open("11_High_Score.txt") as data:
    hiScoreStr = data.read()
    
if hiScoreStr=='':
    with open("11_High_Score.txt", "w") as data:
        data.write(str(score))

elif int(hiScoreStr)<score :
    with open("11_High_Score.txt", "w") as data:
        data.write(str(score))