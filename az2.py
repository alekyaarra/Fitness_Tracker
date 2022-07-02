from tkinter import*

root=Tk()
root.title('Calories input and exercise')

weight=Entry(root, width=30)
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
mybutton4= Button(root, text="Enter your Gender (Male or Female)",  width=35,command=myclick4)
mybutton4.grid(row=3,column=0)
g=gender.get()

def BMRcalc(w,h,a,g):
    global basal
    basal=0
    if str(g).lower()== "male":
        basal=int((10*w)+(6.25*h)-(5*a)+5)
    elif str(g).lower()=="female":
        basal=int((10*w)+(6.25*h)-(5*a)-161)
    mylabel5=Label(root, text="Your Basal Metabolic Rate has been calculated")
    mylabel5.grid(row=5,column=1)
    mylabel5=Label(root, text="Click on 'Daily Calorie Needs' to proceed")
    mylabel5.grid(row=6,column=1)
mybutton5=Button(root,text="Calculate Basal Metabolic rate", command=lambda: BMRcalc(float(weight.get()),float(height.get()),float(age.get()),gender.get()))
mybutton5.grid(row=4,column=1)

def calorie():
    mylabel6=Label(root, text="Enter the appropriate number corresponding\nto your level of exercise")
    mylabel6.grid(row=8,column=1)

    mylabel7=Label(root, text="(1) - Sedentary")
    mylabel7.grid(row=9,column=1)
    mylabel8=Label(root, text="(2) - Exercise 1-3 times a week")
    mylabel8.grid(row=10,column=1)
    mylabel9=Label(root, text="(3) - Exercise 4-5 times a week")
    mylabel9.grid(row=11,column=1)
    mylabel10=Label(root, text="(4) - Daily Exercise or Intense Exercise 3-4 times a week")
    mylabel10.grid(row=12,column=1)
    mylabel11=Label(root, text="(5) - Intense Exercise 6 times a week")
    mylabel11.grid(row=13,column=1)

    calories=Entry(root, width=30)
    calories.grid(row=14, column =1)

    def daily_calorie_needs():
        global totcal
        totcal=0
        cal=int(calories.get())
        if cal==1:
            totcal=1.2*basal
        if cal==2:
            totcal=1.375*basal
        if cal==3:
            totcal=1.46*basal
        if cal==4:
            totcal=1.725*basal
        if cal==5:
            totcal=1.9*basal
        mylabel12=Label(root, text="To maintain your current weight you need\n " + str(int(totcal)) + "calories daily")
        mylabel12.grid(row=16,column=1,)
        mylabel13=Label(root, text="To gain 0.5 kg per week you need\n " + str(int(totcal)+550) + "calories daily")
        mylabel13.grid(row=17,column=1,)
        mylabel14=Label(root, text="To lose 0.5 kg per week you need\n " + str(int(totcal)-550) + "calories daily")
        mylabel14.grid(row=18,column=1,)
    mybutton6=Button(root,text="Calculate Daily Calorie Need", command=daily_calorie_needs)
    mybutton6.grid(row=15,column=1)

mybutton5=Button(root,text="Daily Calorie Needs Calculation", command=calorie)
mybutton5.grid(row=7,column=1)


root.mainloop()