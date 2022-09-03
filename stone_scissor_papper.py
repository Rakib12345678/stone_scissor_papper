import random
l=["rock","scissor","paper"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
  game start......
  1 yes
  2 no|exit   
           '''))
    if uc==1:
         for a in range (1,6):
             userInput=int(input('''
           1 rock
           2 scissor
           3 paper  
             
                     '''))
             if userInput==1:
                 uchoice="rock"
             elif userInput==2:
                 uchoice="scissor"
             elif userInput==3:
                 uchoice = "paper"
             Comchoice=random.choice(l)
             if Comchoice==uchoice:
                 print("computer value",Comchoice)
                 print("user value",uchoice)
                 print("game Draw")
                 ucount =ucount+1
                 ccount =ccount+1
             elif ((uchoice=="rock"and Comchoice=="scissor") or (uchoice=="paper"and Comchoice=="rock") or (uchoice=="scissor"
                and Comchoice == "paper")):
                 print("computer value", Comchoice)
                 print("user value", uchoice)
                 print("you win")
                 ucount=ucount+1
             else:
                print("computer value", Comchoice)
                print("user value", uchoice)
                print("computer win")
                ccount = ccount +1

         if ucount==ccount:
                    print("final game draw...")
                    print("user score",ucount)
                    print("computer score",ccount)

         elif ucount>ccount:
                    print("final you win the game...")
                    print("user score",ucount)
                    print("computer score", ccount)
         else:
            print("final computer win the game...")
            print("user score", ucount)
            print("computer score", ccount)
         break
    else:
        break