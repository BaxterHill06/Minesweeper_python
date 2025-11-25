from tkinter import *
import random

window = Tk()
window.geometry("700x700+20+20")

def makeField(height, width):
    for h in range(height):
        row = []
        for w in range(width):
            row.append(0)
        field.append(row)
    return field


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
    global field
    field = []
    file = open("size.txt", "r")
    for line in file:
        size.append(line.strip("\n"))
    height = int(size[0])
    width = int(size[1])
    numOfBombs = int(size[2])
    field = makeField(height, width)
    field = addBombs(field, height, width, numOfBombs)
    add_Numbers(field, height, width)
    create(height, width)



def btn1function(x,y, height, width):
    global field
    print("x = ", x, "y = ", y)
    state = field[y][x]
    print("state", state)
    if state == 0:
        imgType = image_0
        reveal_0(x,y)
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
        reveal_mines(height, width)
    else:
        imgType = image_0
    replace.config(image=imgType)
    replace.grid(row=y, column=x)


def create(height, width):
    x = 0
    y = 0
    for btn in range(height * width):
        createBtn(x, y, height, width)
        if x == 0:
            print("0")
            x += 1
        elif x%(width-1) == 0:
            x = 0
            y += 1
        else:
            x += 1

#note you can pass x and y throw so no need for z calc

def createBtn(x, y, height, width):
    btn = Button(window, command= lambda: btn.grid_forget() + btn1function(x,y, height, width))
    btn.config(image=image_unknown)
    print("x is", x)
    print("y is", y)
    btn.grid(row=y, column=x)

def reveal_0(x,y):
    space = [-1,0,1]
    space2 = [-1,0,1]
    for column in space:
        print("run column")
        for row in space2:
            checkX = x + row
            checkY = y + column
            reveal(checkX, checkY)


def reveal(x, y):
    global field
    print("this is x and y", x, y)
    if x >= 0 and y >= 0 and x != 0 and y != 0:
        state = field[y][x]
        print("state", state)
        if state == 0:
            imgType = image_0
            replace.config(image=imgType)
            try:
                replace.grid(row=y, column=x)
            except:
                print("not work")
            reveal_0(x,y)
        elif state == 1:
            imgType = image_1
        elif state == 2:
            imgType = image_2
        elif state == 3:
            imgType = image_3
        elif state == 4:
            imgType = image_4
        else:
            imgType = image_0
        replace.config(image=imgType)
        try:
            replace.grid(row=y, column=x)
        except:
            print("not work")
    else:
        print("negitive")


def reveal_mines(height, width):
    global field
    global img_type
    global location
    print("check 0")
    X = 0
    while X < height:
        Y = 0
        while Y < width:
            if field[X][Y] == "mine":
                location = str(X)+ str(Y)
                print("check 1")
                img_type = image_mine
                reveal(x,y)
                print("check 2")
            Y += 1
        X += 1
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



replace = Button(window, text="btn1")

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

run()
