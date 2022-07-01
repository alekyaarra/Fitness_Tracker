from tkinter import*

root=Tk()
root.title('Calories input and exercise')

weight=Entry(root, width=30,)
height=Entry(root,width=30)
age=Entry(root,width=30)
gender=Entry(root,width=30)

weight.grid(row=0,column=1)
def myclick1():
    mylabel1=Label(root, text="Your entered weight is " + weight.get())
    mylabel1.grid(row=0,column=2)
mybutton1= Button(root, text="Enter your weight (in kgs)", width=35, command=myclick1)
mybutton1.grid(row=0,column=0)
w=weight.get()

height.grid(row=1,column=1)
def myclick2():
    mylabel2=Label(root, text="Your entered height is " + height.get())
    mylabel2.grid(row=1,column=2)
mybutton2= Button(root, text="Enter your height (in cms)", width=35, command=myclick2)
mybutton2.grid(row=1,column=0)
h=height.get()

age.grid(row=2,column=1)
def myclick3():
    mylabel3=Label(root, text="Your entered age is " + age.get())
    mylabel3.grid(row=2,column=2)
mybutton3= Button(root, text="Enter your age",  width=35,command=myclick3)
mybutton3.grid(row=2,column=0)
a=age.get()

gender.grid(row=3,column=1)
def myclick4():
    mylabel4=Label(root, text="Your entered gender is " + gender.get())
    mylabel4.grid(row=3,column=2)
mybutton4= Button(root, text="Enter your Gender (male or female)",  width=35,command=myclick4)
mybutton4.grid(row=3,column=0)

basal=0
if gender.get()== "male":
        basal=int((10*w)+(6.25*h)-(5*a)+5)
elif gender.get()=="female":
        basal=int((10*w)+(6.25*h)-(5*a)-161)

mylabel5=Label(root, text="Your Basal Metabolic Rate is " + str(basal))
mylabel5.grid(row=5,column=1)

root.mainloop()