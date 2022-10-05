# GUI-mouse.py
from tkinter import * # Lib: Tk Interface
from tkinter import ttk
import pyautogui as pg
import webbrowser

GUI = Tk()
GUI.title('Calendar')
GUI.geometry('500x300')

def Calendar():
    pg.click(1814,1067)

def News():
    pg.click(1556,1049)

def Google():
    webbrowser.open('https://www.google.com')



B1 = Button(GUI,text='Calendar',command=Calendar)
B1.pack(ipadx=20, ipady=10, pady=20)

B2 = ttk.Button(GUI,text='News',command=News)
B2.pack(ipadx=20, ipady=10, pady=20)

B3 = ttk.Button(GUI,text='Google',command=Google)
B3.pack(ipadx=20, ipady=10)



GUI.mainloop()