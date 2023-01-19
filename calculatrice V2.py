from tkinter import *


def clear():
    valeur.delete(0, END)


def delete():
    valeur.delete(len(valeur.get())-1,END)


def egal():
    result = eval(valeur.get())
    clear()
    valeur.insert(0, result)


def write(k):
    L = ["AC", "√ ", "/", "DEL", "7", "8", "9", "x", "4", "5", "6", "-", "1", "2", "3", "+", "²", "0", ".", "="]
    if L[k] == L[3]:
        delete()
    elif L[k] == L[0]:
        clear()
    elif L[k] == L[7]:
        valeur.insert(END, "*")
    elif L[k] == L[1]:
        valeur.insert(END, "**05")
    elif L[k] == L[16]:
        valeur.insert(END, "**2")
    elif L[k] == L[19]:
        egal()
    else:
        valeur.insert(END, L[k])


window = Tk()
window.title("Calculatrice")
window.geometry("308x480")
window.resizable(FALSE, FALSE)


frame1 = Frame(window, bg="black", width=312, height=500)

frame1.pack(expand=1, fill=BOTH)


# Entry
valeur = Entry(frame1,font=("Arial", 30),bg="black",fg="white")
valeur.pack(fill=BOTH,ipady=41)

# Button

equation = ""
L = ["AC", "√ ", "/", "DEL", "7", "8", "9", "x", "4", "5", "6", "-", "1", "2", "3", "+", "²", "0", ".", "="]
a = 0
b = 130
c = 0
color = "grey"
for i in L:
    button = Button(frame1, text=i, font=("Arial", 18),borderwidth=1, padx=8, fg="white", bg=f"{color}", command=lambda c = c: write(c))
    button.config(width=4,height=2)
    button.place(x=a, y=b)
    a += 77
    c += 1
    color = "grey"
    if c == 3 or c == 7 or c == 11 or c == 15 or c == 19:
        color = "orange"
    if c % 4 == 0:
        a = 0
        b += 70

window.mainloop()
