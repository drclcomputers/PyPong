import keyboard
import os
import time
import random

global run, fps
print("------------------")
print(" PyPong --ver 0.4")
print("------------------\n \n")
print("1. Easy")
print("2. Medium")
print("3. Hard")
print("4. Exit \n \n")
diffask=input("Input option: ")
if diffask=="1":
    fps=17
    run=True
elif diffask=="2":
    fps=30
    run=True
elif diffask=="3":
    fps=50
    run=True
else:
    run=False

score1=0
score2=0
x1=9
x2=9
yb=9
xb=26
def start():
    global bilamiscarex, bilamiscarey
    bilamiscarex=random.randint(0, 1)
    if bilamiscarex==0:
        bilamiscarex=True
    else:
        bilamiscarex=False
    bilamiscarey=random.randint(0, 1)
    if bilamiscarey==0:
        bilamiscarey=True
    else:
        bilamiscarey=False
start()

def paleta1(x1):
    print("\033[%d;%dH" % (x1, 10) + "|")
    print("\033[%d;%dH" % (x1+1, 10) + "|")
    print("\033[%d;%dH" % (x1+2, 10) + "|")

def paleta2(x2):
    print("\033[%d;%dH" % (x2, 40) + "|")
    print("\033[%d;%dH" % (x2+1, 40) + "|")
    print("\033[%d;%dH" % (x2+2, 40) + "|")

while run==True:
    try:
        if keyboard.is_pressed('esc'):
            run=False
        if keyboard.is_pressed('w') and x1>1:
            x1-=1
        if keyboard.is_pressed('s') and x1+2<19:
            x1+=1
        if keyboard.is_pressed('o') and x2>1:
            x2-=1
        if keyboard.is_pressed('l') and x2+2<19:
            x2+=1
        if keyboard.is_pressed('g'):
            yb=9
            xb=26
            x1=9
            x2=9
            score1=0
            score2=0
            start()
    except:
        pass

    if yb==x2 or yb==x2+1 or yb==x2+2:
            if xb==39 or xb==40:
                bilamiscarex=False
    if yb==x1 or yb==x1+1 or yb==x1+2:
            if xb==11:
                bilamiscarex=True
        
    if xb==8:
            yb=9
            xb=26
            x1=9
            x2=9
            score2+=1
            start()
    
    if xb==41:
            yb=9
            xb=26
            x1=9
            x2=9
            score1+=1
            start()

    if bilamiscarex==True:
        if xb<=42:
            xb+=1
        else:
            bilamiscarex=False
    else:
        if xb>=7:
            xb-=1
        else:
            bilamiscarex=True
    
    if bilamiscarey==True:
        if yb<19:
            yb+=1
        else:
            bilamiscarey=False
    else:
        if yb>1:
            yb-=1
        else:
            bilamiscarey=True

    '''#debugging
    print("\033[%d;%dH" % (11, 50) + str(xb))
    print("\033[%d;%dH" % (12, 50) + str(yb))
    print("\033[%d;%dH" % (11, 70) + str(x1))
    print("\033[%d;%dH" % (12, 70) + str(x2))
    #debugging'''

    print("\033[%d;%dH" % (10, 55) + str(score1) + ":" +str(score2))
    for i in range(19):
        print("\033[%d;%dH" % (i+1, 5) + "#")
    for i in range(19):
        print("\033[%d;%dH" % (i+1, 45) + "#")
    for i in range(19):
        print("\033[%d;%dH" % (i+1, 25) + ":")
    paleta1(x1)
    paleta2(x2)
    print("\033[%d;%dH" % (yb, xb) + "o")
    print("\033[%d;%dH" % (20, 1) + "     # # # # # # # # # # # # # # # # # # # # ")
    time.sleep(1./fps)
    os.system("cls")
    
os.system('cls')