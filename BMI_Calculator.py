from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('BMI Calculator')
ws.geometry('1920x1080')
ws.config(bg='light blue')

label_bmi=Label(text="BMI Calculator",font=("Ariel",24),borderwidth=3)
label_bmi.place(x=650,y=100)
label_bmi.config(padx=10,pady=10)

label_bmi2=Label(text='''Your BMI is a measurement that is a ratio of your weight and height. 
It's a good way to gauge whether your weight is in healthy proportion to your height.'''
,font=("HoloLens MDL2 Assets",25,"bold"),bg="light blue")
label_bmi2.place(x=300,y=180)
label_bmi2.config(padx=15,pady=15)

def reset_entry():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 2)
    bmi_index(bmi)

def bmi_index(bmi):
    
    if bmi < 18.5:
        messagebox.showinfo(ws,'BMI-Tracker', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo(ws,'BMI-Tracker', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo(ws,'BMI-Tracker', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo(ws,'BMI-Tracker', f'BMI = {bmi} is Obesity') 
    else:
        messagebox.showerror(ws,'BMI-Tracker', 'something went wrong!')   

var = IntVar()

frame = Frame(
    ws,
    padx=8, 
    pady=8
)
frame.pack(expand=True)


age_lb = Label(
    frame,
    text="Enter Age :",font=("Ariel",10,"bold")
)
age_lb.grid(row=1, column=1)

age_tf = Entry(
    frame, 
)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Select Gender:',font=("Ariel",10,"bold")
)
gen_lb.grid(row=2, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(
    frame2,
    text = 'Male',font=("Ariel",10,"bold"),
    variable = var,
    value = 1
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text = 'Female',font=("Ariel",10,"bold"),
    variable = var,
    value = 2
)
female_rb.pack(side=RIGHT)

height_lb = Label(
    frame,
    text="Enter Height (cm) :  ",font=("Ariel",10,"bold")
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Enter Weight (kg) : ",font=("Ariel",10,"bold")

)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
        frame3,
        text='Calculate',font=("Ariel",10,"bold"),
        command=calculate_bmi
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset',font=("Ariel",10,"bold"),
    command=reset_entry
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Exit',font=("Ariel",10,"bold"),
    command=lambda:ws.destroy()
)
exit_btn.pack(side=RIGHT)

ws.mainloop()
