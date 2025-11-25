from tkinter import *
window = Tk()

def btn1function(btnNum):
    print("it worked", btnNum)




def create():
    z = 1
    x = 0
    y = 0
    for btn in list:
        if x == 0:
            print("0")
        elif x%4 == 0:
            x = 0
            y += 1
        else:
            x += 1
        createBtn(x, y, z)
        z += 1



def createBtn(x, y, z):
    btn = Button(window, text="btn", command= lambda: btn1function(z))
    print("x is", x)
    print("y is", y)
    btn.grid(column=x,row=y)
        

    

list = [1,2,3,4,5,6,7,8,9]


create()

window.mainloop()
