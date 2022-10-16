def PrintBracket(Output, Left, Right, BracketNum):
     if Left == BracketNum and Right == BracketNum:
          ls.append(Output)
     else:
          if Left<BracketNum:
               PrintBracket(Output+"(", Left+1, Right, BracketNum)
          if Right<Left:
               PrintBracket(Output+")", Left, Right+1, BracketNum)
BracketNum = eval(input())
ls=[]
PrintBracket('',0,0,BracketNum)
print(ls)