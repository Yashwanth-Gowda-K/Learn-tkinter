from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(count)
    
window = Tk()

window.geometry('300x200')

button = Button(window,
                text='click here',
                command=click,
                width=20,
                height=4,
                bd=2,
                relief="solid",
                fg="White",
                bg="Black",
                ) 
button.pack(side="bottom")
window.mainloop()