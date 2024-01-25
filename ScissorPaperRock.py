#   Rules as follows
#   Rock vs paper -> paper wins
#   Rock vs scisor -> Rock wins
#   paper vs scissor -> scissor wins.



import random
l=["rock","paper","scissor"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
    Game Start.......
    1 Yes
    2 No | Exit 
    Enter your choice: '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
    1 Rock
    2 Scissor
    3 Paper
        Enter your choice: '''))

            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            Cchoise=random.choice(l)
            if Cchoise==uchoice:
                    print("computer choice: ", Cchoise)
                    print("user choice: ", uchoice)
                    print("Game Draw")
                    ucount=ucount+1
                    ccount=ccount+1
            elif (uchoice=="rock" and Cchoise=="scissor") or (uchoice=="paper" and Cchoise=="rock") or (uchoice=="scissor" and Cchoise=="paper"):
                print("Computer value: ", Cchoise)
                print("user value: ", uchoice)
                print("You win")
                ucount=ucount+1
            else:
                print("Computer value: ", Cchoise)
                print("user value: ", uchoice)
                print("Computer win")
                ccount = ccount + 1
        if ucount==ccount:
            print("Final Game Draw....")
            print("User Score: ", ucount)
            print("Computer Score: ", ccount)
        elif ucount>ccount:
            print("Final You Win the Game ....")
            print("User Score: ", ucount)
            print("Computer Score: ", ccount)
        else:
            print("Final Computer Win the Game ....")
            print("User Score: ", ucount)
            print("Computer Score: ", ccount)

    else:
     break;
