from tkinter import *
import random

window = Tk()
window.geometry("700x700+20+20")

def makeField(height, width, field):
    for h in range(height):
        row = []
        for w in range(width):
            row.append(0)
        field.append(row)
    return field

def revealedArray(height, width, field):
    for h in range(height):
        row = []
        for w in range(width):
            row.append("unknown")
        revealed.append(row)
    return revealed

def addBombs(field, height, width,numOfBombs):

    # random position
    B = 0
    while B < numOfBombs:
        A = 0
        while A == 0:
            Y = random.randint(0, height - 1)
            Z = random.randint(0, width - 1)
            if field[Y][Z] != "mine":
                field[Y][Z] = "mine"
                A = 1
            else:
                print("try")
        B += 1
    print(field)
    return field
    # check if already a bomb before counting as a bomb position
    # if not a bomb, make a bomb, set values around it - setValues()


def add_Numbers(field, height, width):
    X = 0
    while X < height:
        Y = 0
        while Y < width:
            A = -1
            B = -1
            C = X + A
            D = Y + B
            if field[X][Y] == "mine":
                print("spot", field[X][Y])
                print("mine at", X, Y)
                while B < 2:
                    if C > -1 and C < height and D > -1 and D < width:
                        try:
                            print("C",C)
                            print("D", D)
                            field[C][D] += 1
                            print("not mine")
                            print(A)
                            print(B)

                        except:
                            print("mine")
                            print(A)
                            print(B)
                    else:
                        print("fail 1")
                    A +=1
                    if A > 1:
                        A = -1
                        B += 1
                    C = X + A
                    D = Y + B
                    print(field)
            else:
                print("fail 2")
            Y += 1
        X += 1
        print(field)




def run():
    field = []
    file = open("size.txt", "r")
    for line in file:
        size.append(line.strip("\n"))
    height = int(size[0])
    width = int(size[1])
    numOfBombs = int(size[2])
    field = makeField(height, width, field)
    revealedArray(height, width, field)
    field = addBombs(field, height, width, numOfBombs)
    add_Numbers(field, height, width)
    create(height, width, field)



def btn1function(x,y, height, width, field, btn):
    #btn.grid_forget()
    """
    replace = Label(window, text="btn1")
    print("x = ", x, "y = ", y)
    state = field[y][x]
    print("state", state)
    if state == 0:
        imgType = image_0
        reveal_0(x,y, height, width, field)
    elif state == 1:
        imgType = image_1
    elif state == 2:
        imgType = image_2
    elif state == 3:
        imgType = image_3
    elif state == 4:
        imgType = image_4
    elif state == "mine":
        imgType = image_mine
        reveal_mines(x,y,height, width, field)
    else:
        imgType = image_0
    replace.config(image=imgType)
    replace.grid(row=y, column=x)
    revealed[y][x] = "revealed"
    """

def create(height, width, field):
    x = 0
    y = 0
    for btn in range(height * width):
        createBtn(x, y, height, width, field)
        if x == 0:
            print("0")
            x += 1
        elif x%(width-1) == 0:
            x = 0
            y += 1
        else:
            x += 1

#note you can pass x and y throw so no need for z calc

def createBtn(x, y, height, width, field):
    btn = Label(window,image=image_unknown)
    btn.bind("<Button-1>", btn1function(x,y, height, width, field, btn))
    print("x is", x)
    print("y is", y)
    btn.grid(row=y, column=x)

def reveal_0(x,y , height, width, field):
    print(revealed)
    space = [-1,0,1]
    space2 = [-1,0,1]
    for column in space:
        print("run column")
        for row in space2:
            checkX = x + row
            checkY = y + column
            reveal(checkX, checkY, height, width, field)


def reveal(x, y , height, width, field):
    replace = Label(window, text="btn1")
    print("this is x and y", x, y)
    if x >= 0 and y >= 0 and x <= height-1 and y <= width-1:
        if revealed[y][x] == "unknown":
            state = field[y][x]
            print("state", state)
            if state == 0:
                print("entered state 0")
                revealSeperate(x, y, height, width, field)
            elif state == 1:
                imgType = image_1
                replace.config(image=imgType)
            elif state == 2:
                imgType = image_2
                replace.config(image=imgType)
            elif state == 3:
                imgType = image_3
                replace.config(image=imgType)
            elif state == 4:
                imgType = image_4
                replace.config(image=imgType)
            else:
                imgType = image_0
                replace.config(image=imgType)
            try:
                replace.grid(row=y, column=x)
                revealed[y][x] = "revealed"
            except:
                print("not work")
        else:
            print("all ready revealed")
    else:
        print("negitive")


def revealSeperate(x,y, height , width, field):
    replace = Label(window, text="btn1")
    replace.config(image=image_0)
    replace.grid(row=y, column=x)
    revealed[y][x] = "revealed"
    reveal_0(x,y, height ,width, field)



def gridMine(column, row):
    replace = Label(window, text="btn1")
    replace.config(image=image_mine)
    replace.grid(row=column, column=row)


    

def reveal_mines(x,y,height, width, field):
    global img_type
    global location
    print("check 0")
    print(field)
    X = 0
    for column in range(height):
        for row in range(width):
            if field[column][row] == "mine":
                print("row {row}, column {column}".format(column=column, row=row))
                print("check 1")
                gridMine(column, row)
                revealed[column][row] = "revealed"
                print("check 2")
    '''end game'''  

size = []

image_unknown = PhotoImage(file="unknown.gif")
image_flag = PhotoImage(file="flag.gif")
image_0 = PhotoImage(file="empty.gif")
image_1 = PhotoImage(file="1.gif")
image_2 = PhotoImage(file="2.gif")
image_3 = PhotoImage(file="3.gif")
image_4 = PhotoImage(file="4.gif")
image_mine = PhotoImage(file="mine.gif")




revealed = []

run()
window.mainloop()