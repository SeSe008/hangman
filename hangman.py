#!/usr/bin/env python3
#from distutils.log import ERROR
#from itertools import count
from tkinter import *
from PIL import ImageTk, Image
import requests, random

def again():
    global count, WORD, CHARS, CURRENT, label1, button1, panel, ERRORS
    ERRORS=0
    if (count != 0):
        panel.destroy()
    count=0
    button1.destroy()
    label2.destroy()
    try:
        request()
        WORD=word()
    except:
        WORD="NOINTERNET"
    CURRENT.clear()
    CHARS.clear()
    for i in range (0, len(WORD)):
        CURRENT.append("_ ")

        CHARS.append(WORD[i])
    dashes=len(WORD)*"_ "
    label1.configure(text=dashes)

def againq():
    global root, button1
    button1 = Button(root, text='Try again', command=again)
    button1.place(y=5, x=5)

def won():
    global ERRORS, label2
    TXT="You won. You had " + str(ERRORS) + " errors!"
    label2=Label(root, bg="white", fg="black", text=TXT)
    label2.pack()
    againq()

def lose():
    global ERRORS, label2, WORD
    label2 = Label(root, bg="white", fg="black", text="You Lose! The Word was " + WORD +".")
    label2.pack()
    againq()

def request():
    global WORDS, WORD
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(word_site)
    WORDS = response.content.splitlines()

def word():
    global WORDS
    rnd=random.randint(0, 10000)
    WORD=WORDS[rnd]
    WORD=str(WORD)
    WORD=WORD[2:-1].upper()
    return WORD

def manage(event):
    global panel, count, label1, WORD, CHARS, CURRENT, ERRORS
    if (CURRENT.count('_ ')==0):
        return 0
    if (count==15):
        return 0
    key=event.char.upper()
    if (WORD.find(key)==-1):
        count+=1
        ERRORS+=1

        if (count!=1):
            panel.destroy()

        panel=open_img(root)
        if (count==15):
            lose()
            return 0

    else:
        res=""
        for i, j in enumerate(CHARS):
            if j == key:
                CURRENT[i]=key+' '
        for i in range (len(CURRENT)):
            res=res+CURRENT[i]
        label1.configure(text=res)
        if (CURRENT.count('_ ')==0):
            won()
            return 0


def open_img(root):
    global panel, count
    x = "./Pics/H"+str(count)+".png"
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, bg='white', image=img)
    panel.image = img
    panel.pack(side=BOTTOM)
    return panel

def main():
    global count, WORD, CHARS, CURRENT, label1
    try:
        request()
        WORD=word()
    except:
        WORD="NOINTERNET"
    for i in range (0, len(WORD)):
        CURRENT.append("_ ")
        CHARS.append(WORD[i])
    root.geometry("550x300+300+150")
    root.configure(bg='White')
    root.resizable(width=False, height=False)
    dashes=len(WORD)*"_ "
    label1 = Label(bg='white', text=dashes, fg='black')
    label1.pack()
    root.bind("<Key>", manage)
    root.mainloop()

if __name__ == '__main__':
    ERRORS=0
    root=Tk()
    CURRENT=[]
    CHARS=[]
    WORD=""
    WORDS=[]
    panel=""
    count=0
    label2=""
    label1=""
    button1=""
    main()
