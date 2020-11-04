def winGame():
    global game
    global hidden
    
    w = 0
    e = 0
    while w < 10:
        while e < 10:
            if hidden[w][e] != '*':
                game[w+1][e+1] = hidden[w][e]
            e+=1
        e = 0
        w+=1
            
def clearCheck(x,z):
    global game
    global hidden
    
    if hidden[x][z] != '*' and game[x+1][z+1] == '#':
        if hidden[x][z] != '.':
            game[x+1][z+1] = hidden[x][z]
        else:
            game[x+1][z+1] = hidden[x][z]
            spaceClear(x,z) 

def spaceClear(t,y):
    global game
    global hidden
    
    if t-1 > -1:
        if y-1 > -1:
            clearCheck((t-1),(y-1))
        if y+1 < 10:
            clearCheck((t-1),(y+1))
        clearCheck((t-1),y)
        
    if y-1 > -1:
        clearCheck(t,(y-1))
    if y+1 < 10:
        clearCheck(t,(y+1))

    if t+1 < 10:
        if y-1 > -1:
            clearCheck((t+1),(y-1))
        if y+1 < 10:
            clearCheck((t+1),(y+1))       
        clearCheck((t+1),y)
    
    

import random
game = [0,'#','#','#','#','#','#','#','#','#','#']
hidden = [0,0,0,0,0,0,0,0,0,0]

t = 0

while t < 11:
    if t == 0:
        game[t] = ['   ',1,2,3,4,5,6,7,8,9,10]
    else:
        if t != 10:
            game[t] = [str(t)+'  ','#','#','#','#','#','#','#','#','#','#']
        else:
            game[t] = [str(t)+' ','#','#','#','#','#','#','#','#','#','#']
    t+=1
    
t = 0
while t < 10:
    hidden[t] = ['!','!','!','!','!','!','!','!','!','!']
    t+=1
    
t = 0
while t < 11:
    if t==0:
        print(game[t][0],' ',game[t][1],' ',game[t][2],' ',game[t][3],' ',game[t][4],' ',game[t][5],' ',game[t][6],' ',game[t][7],' ',game[t][8],' ',game[t][9],' ',game[t][10])
        print()
    else:
        print(game[t][0],' ',game[t][1],' ',game[t][2],' ',game[t][3],' ',game[t][4],' ',game[t][5],' ',game[t][6],' ',game[t][7],' ',game[t][8],' ',game[t][9],' ',game[t][10])
    t += 1

print()  
inthing = input("Enter Coordinates in the form   (left #):(top #)    ")
print()

userCoords = inthing.split(':')
userCoords[0] = int(userCoords[0])-1
userCoords[1] = int(userCoords[1])-1

hidden[userCoords[0]][userCoords[1]] = '.'

#makes sure no mines around first pick

if userCoords[0]-1 > -1:
    if userCoords[1]-1 > -1:
        hidden[userCoords[0]-1][userCoords[1]-1] = 'c'
    hidden[userCoords[0]-1][userCoords[1]] = 'c'
    if userCoords[1]+1 < 10:
        hidden[userCoords[0]-1][userCoords[1]+1] = 'c'
    
if userCoords[1]-1 > -1:
    hidden[userCoords[0]][userCoords[1]-1] = 'c'
if userCoords[1]+1 < 10:
    hidden[userCoords[0]][userCoords[1]+1] = 'c'

if userCoords[0]+1 < 10:
    if userCoords[1]-1 > -1:
        hidden[userCoords[0]+1][userCoords[1]-1] = 'c'
    hidden[userCoords[0]+1][userCoords[1]] = 'c'
    if userCoords[1]+1 < 10:
        hidden[userCoords[0]+1][userCoords[1]+1] = 'c'


t = random.randint(0,9)
y = random.randint(0,9)

mines = 10 #when this changes change the other one too

while mines != 0:
    if (hidden[t][y] != '.') and (hidden[t][y] != '*') and (hidden[t][y] != 'c'):
        hidden[t][y] = '*'
        mines -= 1
    t = random.randint(0,9)
    y = random.randint(0,9)
    
mines = 10 #resets it for later use. change the one above too
 
#makes every none mine space except first point a point for number insrt algorithm to check    
t = 0
y = 0
while t < 10:
    while y < 10:
        if (hidden[t][y] != '.') and (hidden[t][y] != '*') and (hidden[t][y] != 'c'):
            hidden[t][y] = 'c'
        y += 1
    t += 1
    y = 0
    
#number insert algorithm for hidden board
t = 0
y = 0
MineCount = 0
while t < 10:
    while y < 10:
        if (hidden[t][y] == 'c'):
            if t-1 > -1:
                if y-1 > -1:
                    if hidden[t-1][y-1] == '*':
                        MineCount += 1
                if y+1 < 10:
                    if hidden[t-1][y+1] == '*':
                        MineCount += 1
                if hidden[t-1][y] == '*':
                    MineCount += 1
                
            if y-1 > -1:
                if hidden[t][y-1] == '*':
                    MineCount += 1
            if y+1 < 10:
                if hidden[t][y+1] == '*':
                    MineCount += 1

            if t+1 < 10:
                if y-1 > -1:
                    if hidden[t+1][y-1] == '*':
                        MineCount += 1
                if y+1 < 10:
                    if hidden[t+1][y+1] == '*':
                        MineCount += 1           
                if hidden[t+1][y] == '*':
                    MineCount += 1
            
            if MineCount == 0:
                hidden[t][y] = '.'
            else:
                hidden[t][y] = MineCount
                MineCount = 0
        
        y += 1
    t += 1
    y = 0
    
   


    
#starting the game
spaceClear(userCoords[0],userCoords[1])
             
t = 0
while t < 11:
    if t==0:
        print(game[t][0],' ',game[t][1],' ',game[t][2],' ',game[t][3],' ',game[t][4],' ',game[t][5],' ',game[t][6],' ',game[t][7],' ',game[t][8],' ',game[t][9],' ',game[t][10])
        print()
    else:
        print(game[t][0],' ',game[t][1],' ',game[t][2],' ',game[t][3],' ',game[t][4],' ',game[t][5],' ',game[t][6],' ',game[t][7],' ',game[t][8],' ',game[t][9],' ',game[t][10])
    t += 1
        
#playing the game
thing = True
win = False

while thing:
    print()
    inthing = input("Enter Coordinates in the form   (left #):(top #)    ")
    print()
    
    if inthing == '$SHOW ME THE MONEY$':
        t = 0
        while t < 10:
            print(hidden[t][0],' ',hidden[t][1],' ',hidden[t][2],' ',hidden[t][3],' ',hidden[t][4],' ',hidden[t][5],' ',hidden[t][6],' ',hidden[t][7],' ',hidden[t][8],' ',hidden[t][9])
            t += 1
        inthing = input("Enter Coordinates in the form   (left #):(top #)    ")
    elif inthing == 'I am a total piece of shit, gg I win':
        inthing = input("The next correct move you make wins the game  ")
        winGame()
    
    userCoords = inthing.split(':')
    userCoords[0] = int(userCoords[0])-1
    userCoords[1] = int(userCoords[1])-1
    
    if hidden[userCoords[0]][userCoords[1]] == '*':
        thing = False
        game[userCoords[0]+1][userCoords[1]+1] = hidden[userCoords[0]][userCoords[1]]
    elif hidden[userCoords[0]][userCoords[1]] == '.':
        game[userCoords[0]+1][userCoords[1]+1] = hidden[userCoords[0]][userCoords[1]]
        spaceClear(userCoords[0],userCoords[1])
    else:
        game[userCoords[0]+1][userCoords[1]+1] = hidden[userCoords[0]][userCoords[1]]
        
    t = 0
    while t < 11:
        if t==0:
            print(game[t][0],' ',game[t][1],' ',game[t][2],' ',game[t][3],' ',game[t][4],' ',game[t][5],' ',game[t][6],' ',game[t][7],' ',game[t][8],' ',game[t][9],' ',game[t][10])
            print()
        else:
            print(game[t][0],' ',game[t][1],' ',game[t][2],' ',game[t][3],' ',game[t][4],' ',game[t][5],' ',game[t][6],' ',game[t][7],' ',game[t][8],' ',game[t][9],' ',game[t][10])
        t += 1
        
    print()
    
    NumberOSpaces = 0
    x = 1
    p = 1
    while x < 11:
        while p < 11:
            if game[x][p] == '#':
                NumberOSpaces += 1
            p+=1
        p=1
        x+=1
        
    if NumberOSpaces == mines:
        win = True
        thing = False

if win == True:
    print("\n\n\nYou won get a cookie! Remember: you aren't special.")
else:
    print("\n\n\nYou lose. That's a mine. Go kick a rock.")
    
print()
print()
input()
