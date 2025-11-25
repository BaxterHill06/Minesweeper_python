from tkinter import *
window = Tk()

def btn1function(btnNum):
    print("it worked", btnNum)
    replace = Label(window,text="replace")
    print("x" , (btnNum-1)%4)
    print("y", (btnNum-1)//4)
    replace.grid(row=(btnNum-1)//4, column=(btnNum-1)%4)



def create():
    z = 1
    x = 0
    y = 0
    for btn in list:
        createBtn(x, y, z)
        if x == 0:
            print("0")
            x += 1
        elif x%3 == 0:
            x = 0
            y += 1
        else:
            x += 1
        z += 1



def createBtn(x, y, z):
    btn = Button(window, text="btn", command= lambda: btn.grid_forget() + btn1function(z))
    print("x is", x)
    print("y is", y)
    btn.grid(row=y, column=x)
        

replace = Button(window, text="btn1")

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


create()

window.mainloop()
