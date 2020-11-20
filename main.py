from termcolor import colored
import sys




class Game():

    def __init__(self):
        self.row1 = ['-', '-', '-']
        self.row2 = ['-', '-', '-']
        self.row3 = ['-', '-', '-']

    def showBoard(self):
        print(self.row1)
        print(self.row2)
        print(self.row3)

    def inputChecker(self,input):
        try:
            x, y = input[0]
        except:
            return {"status":False,"message":"problem with input - please input like this (1,3) it means first row and third colum","code":1}
        try:
            if x.isdigit() is False or y.isdigit() is False:
                return {"status":False,"message":"please enter number you can't enter alphabetic","code":2}
        except:
            return {"status":False,"message":"problem with input","code":3}

        return {"status":True,"message":"ok","code":0}


    def playGame(self,userinput):
        checksts = self.inputChecker(userinput)
        if checksts["status"]:
            x=int(userinput[0][0])
            y = int(userinput[0][1])
            player=userinput[1]
            if x==1:
                if self.row1[y-1]=='-':
                    self.row1[y-1]=player
                    return True
                return False
            if x==2:
                if self.row2[y-1] == '-':
                    self.row2[y-1] = player
                    return True
                return False
            if x==3:
                if self.row3[y-1] == '-':
                    self.row3[y-1] = player
                    return True
                return False
        else:
            print(checksts["message"])
            return False

    def checkWining(self,curuser):
        win=False
        i=0
        if (self.row1[i] ==curuser and self.row1[i+1] ==curuser and self.row1[i+2] ==curuser) or (self.row2[i] ==curuser and self.row2[i+1] ==curuser and self.row2[i+2] ==curuser) or (self.row2[i] ==curuser and self.row2[i+1] ==curuser and self.row2[i+2] ==curuser):
            win=True
        if (self.row1[i] == curuser and self.row2[i] == curuser and self.row3[i] == curuser) or (
                self.row1[i+1] == curuser and self.row2[i + 1] == curuser and self.row3[i + 1] == curuser) or (
                self.row1[i+2] == curuser and self.row2[i + 2] == curuser and self.row3[i + 2] == curuser):
            win = True
        if (self.row1[i] == curuser and self.row2[i+1] == curuser and self.row3[i+2] == curuser) or (
                self.row1[i+2] == curuser and self.row2[i + 1] == curuser and self.row3[i] == curuser):
            win = True
        return win,curuser


game=Game()
sts=True
player=['X','O']
i=0
ut1=False
ut2=False
while sts:
    while ut1 is False:
        print(colored(f"now player {player[i]} ----------------------------------------------","green"))
        inputs=input("xy=")
        x=inputs[0]
        y=inputs[1]
        ut=game.playGame([(x,y),player[i]])
        if ut is False:
            print(f"Error by user {player[i]} !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ")
        if ut is True:
            ut2=False
            game.showBoard()
            if game.checkWining(player[i])[0]:
                print(f"player {player[i]} win the game")
                sys.exit()
            ut1 = True

    while ut2 is False:
        print(colored(f"now player {player[i+1]} ----------------------------------------------","red"))
        inputs=input("xy=")
        x=inputs[0]
        y=inputs[1]
        ut2 = game.playGame([(x, y), player[i+1]])
        if ut2 is False:
            print(f"Error by user {player[i+1]} !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        if ut2 is True:
            ut1=False
            game.showBoard()
            if game.checkWining(player[i+1])[0]:
                print(f"player {player[i+1]} win the game")
                sys.exit()
            ut2 = True
