
from tkinter import *
from turtle import left, right
from PIL import ImageTk, Image

window=Tk()
window.title("A Helping Hand Toward Your Radient Health")
window.geometry("1920x1080")
window.config(padx=10,pady=10)

my_pic=Image.open("health4.jpg")
resized=my_pic.resize((1500,800),Image.ANTIALIAS)
new_pic=ImageTk.PhotoImage(resized)

my_label=Label(window,image=new_pic)
my_label.pack()

my_text=Label(window,text='''      An activity tracker, also known as a fitness tracker,is a device 
                    or application for monitoring and tracking fitness-related metrics 
            such as distance walked or run,
            calorie consumption,BMI tracker,etc...''',background="light blue",font=("Comic Sans MS",15,"italic"))
my_text.place(x=400,y=300)

def button_clicked():
    new_window=Tk()
    new_window.geometry("1920x1080")
    new_window.pack()
    new_window.mainloop()

my_button=Button(text="Yes2LiveHealthy",font=("Comic Sans MS",15,"bold"),command=button_clicked)
my_button.place(x=700,y=600)
window.mainloop()
