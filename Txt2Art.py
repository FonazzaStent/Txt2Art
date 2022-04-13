import os
import turtle
import tkinter as TK

text= open("text.txt")



line=["A","I","K","L","M","N","Z","k","z","V","W","X","Y","v","w","x","y","E","F","f","h","i","l","m","n","t"]
curve=["B","D","J","O","P","Q","b","j","o","p","C","G","R","S","U","a","c","d","e","g","q","s","u"]
lenline= len(line)
lencurve=len(curve)
linecurve=1

def iterationsfn():
    inputiterations=input("Iterations (1 to 100, 0 to quit program): ")
    if (inputiterations.isdigit()):
        iterationvalue=int(inputiterations)
        if iterationvalue>100:
            iterationvalue=100
        if iterationvalue<0:
            iterationvalue=1
        if iterationvalue==0:
            quit()

    else:
        iterationvalue=1
    return iterationvalue

def iterationspacefn():   
    inputiterationspace=input("Space between iterations (1 to 500): ")
    if (inputiterationspace.isdigit()):
        iterationspacevalue=int(inputiterationspace)
        if iterationspacevalue>500:
            iterationspacevalue=500
        if iterationspacevalue<1:
            iterationspacevalue=1
    else:
        iterationspacevalue=1
    return iterationspacevalue        

def directionfn():
    inputdirection=input("Direction (left=1, right=2): ")
    if (inputdirection.isdigit()):
        directionvalue=int(inputdirection)
        if directionvalue<1:
            directionvalue=1
        if directionvalue>2:
            directionvalue=2
    else:
        directionvalue=2
    return directionvalue

def parameters():
    iterations()
    iterationspace()
    direction()

turtle.setup (width=640, height=480, startx=0, starty=0)
turtle.speed(0)

def end():
    text.close

def draw(lencurve,linecurve):
    for pixels in range (1,linesnumber):
        char=text.read(1)
        asciicode=ord(char)
        if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123):
            for n in range (lencurve):
                if char==curve[n]:
                    linecurve=2
            if linecurve==1:
                turtle.forward(asciicode)
                turtle.left(asciicode)
            else:
                turtle.circle(asciicode,asciicode)
            linecurve=1
            if turtle.xcor()>320:
                turtle.setx(320)
            if turtle.xcor()<-320:
                turtle.setx(-320)
            if turtle.ycor()>240:
                turtle.sety(240)
            if turtle.ycor()<-240:
                turtle.sety(-240)
def repeat():
    for n in range(iterations):
        draw(lencurve,linecurve)
        turtle.forward(iterationspace)
        if direction==1:
            turtle.left(iterationspace)
        else:
            turtle.right(iterationspace)
        text.seek(0,0)

loop=1
while (loop==1):
    filelength=text.read()
    linesnumber=len(filelength)+1
    if linesnumber<1:
        linesnumber=1
    if linesnumber>10000:
        linesnumber=10000
    text.seek(0,0)
    iterations=iterationsfn()
    iterationspace=iterationspacefn()
    direction=directionfn()
    repeat()
    clearscreeninput=input("Clear screen? (yes=1 no=0)")
    if clearscreeninput.isdigit():
        clearscreen=int(clearscreeninput)
        if clearscreen<0 or clearscreen>1:
            clearscreen=0
        if clearscreen==1:
            turtle.clear()
TK.mainloop()
