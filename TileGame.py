import random
box = []
blankboom = "  "
score = 0
totalscore = 0


def creatingemptybox():
    for i in range(6):
        row=[blankboom for j in range(6)]
        box.append(row)
        print("-"*6)

    for row in box:
        print("| " + " | ".join(row) + " |")
        print("-"*30)
    print("  ")    

    for i in range(6):
        row = random.randint(0,5)
        column = random.randint(0,5)

        box[row][column] = "*"
    print(box)
    print(" ")

restart = True
countingame = True                

def insidegame():
    global score, totalscore, restart,countingame

    while restart: 
        for i in range(31):
            try:
                userchoice1 = int(input("enter row number : "))
                userchoice2 = int(input("enter column number : "))
            except Exception:
                print("Enter correct row and column")
                continue

            if box[userchoice1][userchoice2] == "*":
               print("game over") 
               totalscore += score
               score = 0
               print("your current score : ",totalscore)

               ch = input("want to countinue the game True/False :").capitalize() 
               if  ch =="False": 
                    countingame = False
                    return 1
               else :
                   countingame = True
                   return 1
            else:
                score +=1
                print("current score : ",score)   

                if score == 31:
                    score =0
                    print("you won") 
                    print("")

while countingame:
    creatingemptybox()
    insidegame()
else:
    print("total score",totalscore)