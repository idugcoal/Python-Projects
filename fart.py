#!/usr/bin/env python
from Tkinter import *
def messageWindow() :
    win = Toplevel()
    b = Button(win, text='DING DING DING',
         bg="blue", fg="yellow",
         activebackground="red", activeforeground="white",
         padx=root.winfo_screenwidth()/2,
         pady=root.winfo_screenheight()/2,
         command=quit)
    b.pack()


    def show_alert() :
        root.bell()
        messageWindow()
    
    def start_timer() :
        root.after(scale.get() * 1000, show_alert)
  

  
   
  
   
   
    button.grid(row=1, column=1, pady=5, sticky=E)

    root.mainloop()