import tkinter as tk
from tkinter import Button
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        btn0=tk.Button(self,text="0")
        btn0.pack(side=tk.LEFT,padx=(0,0),pady=(5,5))
        btn1=tk.Button(self,text="1")
        btn1.pack(side=tk.LEFT,padx=(0,0),pady=(5,5))
        btn2=tk.Button(self,text="2")
        btn2.pack(side=tk.LEFT,padx=(0,0),pady=(5,5))
        btn3=tk.Button(self,text="3")
        btn3.pack(side=tk.LEFT,padx=(0,0),pady=(5,5))
        btn4=tk.Button(self,text="4")
        btn4.pack()
        btn5=tk.Button(self,text="5")
        btn5.pack()
        btn6=tk.Button(self,text="6")
        btn6.pack()
        btn7=tk.Button(self,text="7")
        btn7.pack()
        btn8=tk.Button(self,text="8")
        btn8.pack()
        btn9=tk.Button(self,text="9")
        btn9.pack() 
    def button(self):
        self    
def main():
    window=Window()
    window.title("計算機")
    window.mainloop()
if __name__ =="__main__":
    main()