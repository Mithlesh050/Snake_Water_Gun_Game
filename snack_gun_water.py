import random
def game(a , b):
    if a==b :
        return None
    elif a == 's' :
        if(b=='w'):
            return False
        else:
            return True
    elif a=='w':
        if b=='g' :
            return False
        else:
            return True
    elif a=='g' :
        if b=='w':
            return True
        else:
            return False  

print("Computer turn : Select Snack(1) , Gun(2) and Water(3)?")
ran = random.randint(1 , 3)
if(ran == 1):
    comp = 's' 
elif(ran == 2):
    comp = 'g'
else:
    comp = 'w'
# print(comp)

you = input("Your turn : select Snack(s) , Gun(g) and Water(w)? : ")
v = game(comp , you)

if(v==False):
    print("You loose the game 💔💔💔")
elif(v==True):
    print("You won the game 💖💖💖")
else:
    print("Game is draw 💕💕💕")

