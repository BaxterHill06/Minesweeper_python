from tkinter import *
import random

window = Tk()
window.geometry("300x400+500+20")

def makeField(height, width):
    for h in range(height):
        row = []
        for w in range(width):
            row.append(0)
        field.append(row)
    return field


def addBombs(field, height, width):

    numOfBombs = 3
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
    height = 4
    width = 4
    field = makeField(height, width)
    field = addBombs(field, height, width)
    add_Numbers(field, height, width)
    create(height, width)



def btn1function(btnNum, width):
    print("it worked", btnNum)
    replace = Label(window,text="replace")
    x = int((btnNum-1)%width)
    y = int((btnNum-1)//width)
    state = field[x][y]
    print("state", state)
    if state == 0:
        imgType = image_0
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
    else:
        imgType = image_0
    replace.config(image=imgType)
    replace.grid(row=(btnNum-1)//4, column=(btnNum-1)%4)
    reveal_0(x,y)


def create(height, width):
    z = 1
    x = 0
    y = 0
    for btn in range(height * width):
        createBtn(x, y, z, width)
        if x == 0:
            print("0")
            x += 1
        elif x%(width-1) == 0:
            x = 0
            y += 1
        else:
            x += 1
        z += 1

#note you can pass x and y throw so no need for z calc

def createBtn(x, y, z, width):
    btn = Button(window, command= lambda: btn.grid_forget() + btn1function(z, width))
    btn.config(image=image_unknown)
    print("x is", x)
    print("y is", y)
    btn.grid(row=y, column=x)

def reveal_0(x,y):
    global field
    D = int(x)
    E = int(y)
    H = D
    I = E
    print("sgjrgbsruh")
    F = 0
    G = -1
    A = E + F
    B = D + G
    while I < E + 1:
        A = H + F
        B = I + G
        if field[A][B] == 0:
            entry = field[A][B]
            '''pickImage(entry)'''
        if H == D and I == E:
            H -= 1
        elif H == D - 1 and I == E:
            H += 2
        elif H == D + 1 and I == E:
            H = D
            I -= 1
        elif I == E - 1:
            I += 2
        print("e", E)
        print("I", I)


def reveal_mines():
    global field
    global img_type
    global location
    print("check 0")
    X = 0
    while X < 4:
        Y = 0
        while Y < 4:
            if field[X][Y] == "mine":
                location = str(X)+ str(Y)
                print("check 1")
                img_type = image_mine
                sort_location()
                print("check 2")
            Y += 1
        X += 1
    '''end game'''



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




