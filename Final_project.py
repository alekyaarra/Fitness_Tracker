from tkinter import *
from turtle import left, right
from PIL import ImageTk, Image
from tkinter import messagebox
from cProfile import label
from tkinter import ttk

window=Tk()
window.title("A Helping Hand Toward Your Radiant Health")
window.geometry("1920x1080")
window.config(padx=10,pady=10)

my_pic=Image.open("health4.jpg")
resized=my_pic.resize((1500,800),Image.ANTIALIAS)
new_pic=ImageTk.PhotoImage(resized)

my_label=Label(window,image=new_pic)
my_label.pack()

logo=Image.open("logo2.png")
resize_l=logo.resize((150,150),Image.ANTIALIAS)
new_logo=ImageTk.PhotoImage(resize_l)
logo_button=Button(window,image=new_logo,bg="light blue",borderwidth="10")
logo_button.place(x=700,y=400)

my_text=Label(window,text=''' The best INVESTMENT you can ever make
is in your OWN HEALTH ''',background="light blue",font=("century",20,"bold"))
my_text.place(x=500,y=250)
my_text.config(padx=10,pady=10)

def button_clicked():
    global new_window
    global logo2
    global icon 

    new_window=Toplevel(window)
    new_window.title("A Helping Hand Toward Your Radiant Health")
    new_window.geometry("1920x1080")
    new_window.config(bg="#eaebc3")

    logo2=ImageTk.PhotoImage(Image.open("bg6.png"))
    Label(new_window, image=logo2).pack()
    
    
    app_des=Label(new_window,text='''      An activity tracker, also known as a fitness tracker,is a device 
            or application for monitoring and tracking fitness-related metrics 
            such as distance walked or run,
            calorie consumption,BMI tracker,etc...''',font=("Tempus Sans ITC",20,"bold"))
    app_des.place(x=0,y=200)
    app_des.config(padx=10,bg="#eaebc3")
    
    app_title=Label(new_window,text="Fitness Tracker",font=("Tempus Sans ITC",40,"bold"),bg="#eaebc3")
    app_title.place(x=300,y=100)
    
    icon=ImageTk.PhotoImage(Image.open("C:/Users/tejal/Downloads/fitlogo (1).jpg"))

    Button(new_window, image=icon,borderwidth="3",bg="black").place(x=200, y=100)
    
    def button1_clicked(): 
        global ws
        global label_bmi
        global label_bmi2

        ws = Tk()
        ws.title('BMI Calculator')
        ws.geometry('1920x1080')
        ws.config(bg='light blue')

        label_bmi=Label(ws,text="BMI Calculator",font=("Ariel",24),borderwidth=3)
        label_bmi.place(x=650,y=100)
        label_bmi.config(padx=10,pady=10)

        label_bmi2=Label(ws,text='''Your BMI is a measurement that is a ratio of your weight and height. 
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
                messagebox.showinfo('BMI-Tracker', f'BMI = {bmi} is Underweight')
            elif (bmi > 18.5) and (bmi < 24.9):
                messagebox.showinfo('BMI-Tracker', f'BMI = {bmi} is Normal')
            elif (bmi > 24.9) and (bmi < 29.9):
                messagebox.showinfo('BMI-Tracker', f'BMI = {bmi} is Overweight')
            elif (bmi > 29.9):
                messagebox.showinfo('BMI-Tracker', f'BMI = {bmi} is Obesity') 
            else:
                messagebox.showerror('BMI-Tracker', 'something went wrong!')   
            ws.mainloop()
        var = IntVar()

        frame = Frame(
           ws,
           padx=10, 
           pady=10
        )
        frame.pack(expand=True)


        age_lb = Label(
           frame,
           text=" Enter Age :",font=("Ariel",10,"bold")
        )
        age_lb.grid(row=1, column=1)

        age_tf = Entry(
            frame, 
        )
        age_tf.grid(row=1, column=2, pady=5)

        gen_lb = Label(
            frame,
            text='Select Gender',font=("Ariel",10,"bold")
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
            text="Enter Height (cm): ",font=("Ariel",10,"bold")
        )
        height_lb.grid(row=3, column=1)

        weight_lb = Label(
            frame,
            text="Enter Weight (kg): ",font=("Ariel",10,"bold")

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

        ws.mainloop
            
    def button2_clicked():
        root=Tk()
        root.title('Calories input and exercise')
        root.geometry("700x500")

        weight=Entry(root, width=30)
        height=Entry(root,width=30)
        age=Entry(root,width=30)
        gender=Entry(root,width=30)

        weight.grid(row=0,column=1)
        def myclick1():
            mylabel1=Label(root, text="Your entered weight is " + weight.get())
            mylabel1.grid(row=0,column=2)
        mybutton1= Button(root, text="Enter your weight (in kgs)", width=35)
        mybutton1.grid(row=0,column=0)
        w=weight.get()

        height.grid(row=1,column=1)
        def myclick2():
            mylabel2=Label(root, text="Your entered height is " + height.get())
            mylabel2.grid(row=1,column=2)
        mybutton2= Button(root, text="Enter your height (in cms)", width=35)
        mybutton2.grid(row=1,column=0)
        h=height.get()

        age.grid(row=2,column=1)
        def myclick3():
            mylabel3=Label(root, text="Your entered age is " + age.get())
            mylabel3.grid(row=2,column=2)
        mybutton3= Button(root, text="Enter your age",  width=35)
        mybutton3.grid(row=2,column=0)
        a=age.get()

        gender.grid(row=3,column=1)
        def myclick4():
            mylabel4=Label(root, text="Your entered gender is " + gender.get())
            mylabel4.grid(row=3,column=2)
        mybutton4= Button(root, text="Enter your Gender (Male or Female)",  width=35)
        mybutton4.grid(row=3,column=0)
        g=gender.get()

        def BMRcalc(w,h,a,g):
            global basal
            basal=0
            if str(g).lower()== "male":
                basal=int((10*w)+(6.25*h)-(5*a)+5)
            elif str(g).lower()=="female":
                basal=int((10*w)+(6.25*h)-(5*a)-161)
            mylabel5=Label(root, text="   Your Basal Metabolic Rate is "+str(basal),width=35)
            mylabel5.grid(row=5,column=1)
            mylabel5=Label(root, text="Click on 'Daily Calorie Needs' to proceed")
            mylabel5.grid(row=6,column=1)
        mybutton5=Button(root,text="Calculate Basal Metabolic rate",width=35, command=lambda: BMRcalc(float(weight.get()),float(height.get()),float(age.get()),gender.get()))
        mybutton5.grid(row=4,column=0)

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
            mybutton6=Button(root,text="Calculate Daily Calorie Need",width=35, command=daily_calorie_needs)
            mybutton6.grid(row=15,column=0)

        mybutton5=Button(root,text="Daily Calorie Needs Calculation",width=35, command=calorie)
        mybutton5.grid(row=7,column=0)


        root.mainloop()
    def button3_clicked():
        def open_wl():
            style= ttk.Style()
            style.theme_use('clam')

            top=Toplevel()
            top.title("Weight loss")
            top.state("zoomed")
            label=Label(top,text="Tips to lose Weight in a Healthy Way:",font=15)
            label.pack(anchor=NW)
            l1=Label(top,text="\n  1.Cardohydrates should make up half of your daily calorie requirement")
            l2=Label(top,text="  2.Your diet should consist of 30 percent of protein")
            l3=Label(top,text="  3.Your diet must consist of 20 percent of healthy fats")
            l4=Label(top,text="  4.Vitamins like A, E, B12, D, calcium and iron\n")

            l1.pack(anchor=NW)
            l2.pack(anchor=NW)
            l3.pack(anchor=NW)
            l4.pack(anchor=NW)
    
            l7=Label(top,text="Diet plan to lose weight:\n",font=20)
            l7.pack(anchor=CENTER)

            tree_frame=Frame(top)
            tree_frame.pack(pady=20)
            tree_scroll = ttk.Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT,fill=Y)
            my_tree=ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)

            my_tree['columns']=('Day','food_pre_breakfast','food_breakfast','food_pre_lunch','food_lunch','food_snacks', 'food_dinner')

            my_tree.column("#0", width=20,  minwidth=25)
            my_tree.column("Day",anchor=CENTER,width=30)
            my_tree.column("food_pre_breakfast",anchor=CENTER, width=150)
            my_tree.column("food_breakfast",anchor=CENTER, width=150)
            my_tree.column("food_pre_lunch",anchor=CENTER, width=150)
            my_tree.column("food_lunch",anchor=CENTER, width=150)
            my_tree.column("food_snacks",anchor=CENTER, width=150)
            my_tree.column("food_dinner",anchor=CENTER, width=300)
    
            my_tree.heading("#0", text='', anchor=CENTER)
            my_tree.heading("Day",text="Day", anchor=CENTER)
            my_tree.heading("food_pre_breakfast",text="Pre Breakfast", anchor=CENTER)
            my_tree.heading("food_breakfast",text='Breakfast', anchor=CENTER)
            my_tree.heading("food_pre_lunch",text='Pre Lunch', anchor=CENTER)
            my_tree.heading("food_lunch",text='Lunch', anchor=CENTER)
            my_tree.heading("food_snacks",text='Snacks', anchor=CENTER)
            my_tree.heading("food_dinner",text='Dinner', anchor=CENTER)

            food=[
                ['1','Cucumber Detox Water','Oats Porridge in Skimmed Milk','Skimmed Milk Panner','Dal,Gajar Matar Sabzi,Roti','Cut Fruits, Buttermilk','Dal,Lauki Sabzi,Roti'],
                ['2','Cucumber Detox Water','Curd, Mixed Vegetable Stuffed Roti','Skim Milk Yoghurt','Lentil Curry,Methi Rice','Apple,buttermillk','Sauteed Vegetables with Paneer,Roti'],
                ['3','Cucumber Detox Water','Skim Milk Yoghurt, Multigrain Toast','Skimmed Milk Panner','Sauteed Vegetables with Paneer,Roti','Banana,Buttermilk','Lentil Curry, Methi Rice'],
                ['4','Cucumber Detox Water','Fruit and Nuts Yogurt Smoothie','Skim Milk Yoghurt','Green Gram Whole Dal Cooked,Bhindi sabzi','Orange, Buttermilk','Palak Chole, Steamed Rice'],
                ['5','Cucumber Detox Water','Skimmed Milk, Peas Poha','Skimmed Milk Panner','Low Fat Paneer Curry, Missi Roti','Papaya, Buttermilk','Curd, Aloo Baingan Tamatar Ki Sabzi'],
                ['6','Cucumber Detox Water','Mixed Sambar, Idli','Skim Milk Yoghurt','Curd, Aloo Baingan Tamatar Ki Sabzi','Cut Fruits, Buttermilk','Green Gram Whole Dal Cooked, Bhindi sabzi'],
                ['7','Cucumber Detox Water','Besan Chilla','Skimmed Milk Panner','Palak Chole, Steamed Rice','Apple, Buttermilk','Low Fat Paneer Curry, Missi Roti']
            ]

            count=0
            for i in food:
                my_tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
                count+=1

            a=7
            my_tree.insert(0,index='end',iid=a,values=('','nearly 0 cal','200cal per serving','215cal per 30g','157cal in 1 1/2 cup','200cal per serving','100cal per 50g'),tags='child')
            my_tree.insert(1,index='end',iid=(a+1),values=('','nearly 0 cal','200cal per serving','137cal in 1 cup','250cal per serving','50 cal per 100 ml','250 cal per serving'),tags='child')
            my_tree.insert(2,index='end',iid=(a+2),values=('','nearly 0 cal','230cal per serving','215cal per 30','200cal per serving','68 cal per 100 ml','350 cal per serving'),tags='child')
            my_tree.insert(3,index='end',iid=(a+3),values=('','nearly 0 cal','200cal per serving','137cal in 1 cup','200cal per serving','57 cal per 100 ml','300 cal per serving'),tags='child')
            my_tree.insert(4,index='end',iid=(a+4),values=('','nearly 0 cal','220cal per serving','215cal per 30','300cal per serving','62 cal per 100 ml','220 cal per serving'),tags='child')
            my_tree.insert(5,index='end',iid=(a+5),values=('','nearly 0 cal','250cal per serving','137cal in 1 cup','220cal per serving','55 cal per 100 ml','250 cal per serving'),tags='child')
            my_tree.insert(6,index='end',iid=(a+6),values=('','nearly 0 cal','150cal per serving','215cal per 30','200cal per serving','50 cal per 100 ml','230 cal per serving'),tags='child')

            my_tree.tag_configure('child',background='#DACEB7' )
            my_tree.pack()
            tree_scroll.config(command=my_tree.yview)

            l8=Label(top,text="your total colorie intake per week = 1500 x 7 cal = 10,500 cal")
            l8.pack(anchor=CENTER)
            top.mainloop()

        def open_wg():
            style= ttk.Style()
            style.theme_use('clam')

            top=Toplevel()
            top.state('zoomed')
            top.title("Weight gain")
            root.title('diet plan')
            label=Label(top,text="Tips to Gain Weight in a Healthy Way:",font=15)
            label.pack(anchor=NW)
            l1=Label(top,text="\n  1.High-Calorie Food")
            l2= Label(top,text="  2.Consume Healthy Carbs")
            l3= Label(top,text="  3.Protein Rich Food")
            l4= Label(top,text="  4.Reduce Stress")
            l5= Label(top,text="  5.Strength Training")
            l6= Label(top,text="  6.Get Good Sleep\n")
            l1.pack(anchor=NW)
            l2.pack(anchor=NW)
            l3.pack(anchor=NW)
            l4.pack(anchor=NW)
            l5.pack(anchor=NW)
            l6.pack(anchor=NW)

            l7=Label(top,text="Diet plan for weight gain\n",font=15)
            l7.pack(anchor=CENTER)

            tree_frame=Frame(top)
            tree_frame.pack(pady=20)
            tree_scroll = ttk.Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT,fill=Y)
            my_tree=ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)

            my_tree['columns']=('Day','food_pre_breakfast','food_breakfast','food_pre_lunch','food_lunch','food_snacks', 'food_dinner')

            my_tree.column("#0", width=20,  minwidth=25)
            my_tree.column("Day",anchor=CENTER,width=30)
            my_tree.column("food_pre_breakfast",anchor=CENTER, width=150)
            my_tree.column("food_breakfast",anchor=CENTER, width=150)
            my_tree.column("food_pre_lunch",anchor=CENTER, width=150)
            my_tree.column("food_lunch",anchor=CENTER, width=300)
            my_tree.column("food_snacks",anchor=CENTER, width=150)
            my_tree.column("food_dinner",anchor=CENTER, width=300)
    
            my_tree.heading("#0", text='', anchor=CENTER)
            my_tree.heading("Day",text="Day", anchor=CENTER)
            my_tree.heading("food_pre_breakfast",text="Pre Breakfast", anchor=CENTER)
            my_tree.heading("food_breakfast",text='Breakfast', anchor=CENTER)
            my_tree.heading("food_pre_lunch",text='Pre Lunch', anchor=CENTER)
            my_tree.heading("food_lunch",text='Lunch', anchor=CENTER)
            my_tree.heading("food_snacks",text='Snacks', anchor=CENTER)
            my_tree.heading("food_dinner",text='Dinner', anchor=CENTER)

            food=[
                [1,'Almonds soaked overnight','Oats Banana Pancakes','Coconut water','Multigrain roti along with palak chicken','Bananas','Brown rice, peas paneer curry, sprouts vegetable salad'],
                [2,'Almonds soaked overnight','Oatmeal with Greek Yogurt & Seasonal fruits','Lassi','Multigrain roti, fish curry/vegetable curry','Toast with Jam','Broken wheat khichidi along with egg white'],
                [3,'Almonds soaked overnight','Poached Eggs, Protein Shake','Buttermilk','Quinoa upma, chicken and broccoli salad','Mixed Nuts & Dried Fruits','vegetable curry, brown rice, cucumber raita'],
                [4,'Almonds soaked overnight','Oatmeal with Honey','Coconut water','Grilled Chicken/Salad & Whole Grain Bread','Toast with Peanut Butter','Methi Chicken/Brown Rice, Broccoli, Protein Shake'],
                [5,'Almonds soaked overnight','Scrambled Egg & Smoothie','Lassi','(Grilled chicken) vegetable roti rolls Green Salad','Mixed Nuts & Dried Fruits','Spring Onion, Peppers & Broccoli Chocolate Milk'],
                [6,'Almonds soaked overnight','Oatmeal & Orange Juice','Buttermilk','Black Beans, Peppers & Greek Yogurt','Apple with peanut butter','Sweet Potato Protein Shake'],
                [7,'Almonds soaked overnight','Oatmeal with Nuts Smoothie','Coconut water','Whole wheat (pasta with chicken) and Green Salad','Granola or Cereal','boiled green peas salad with Brown Rice']
            ]

            count=0
            for i in food:
                my_tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
                count+=1
    
            a=7
            my_tree.insert(0,index='end',iid=a,values=('','7cal per almond','71cal per pancake','19cal per 100ml','200cal per serving','105cal','300cal'),tags='child')
            my_tree.insert(1,index='end',iid=(a+1),values=('','7cal per almond','100cal per serving','112cal per 100 ml','200cal per serving','50cal','250cal'),tags='child')
            my_tree.insert(2,index='end',iid=(a+2),values=('','7cal per almond','57cal per egg','20cal per 200 ml','100cal per 250g','50cal per 25g','250cal per serving'),tags='child')
            my_tree.insert(3,index='end',iid=(a+3),values=('','7cal per almond','100cal','19cal p            r 100ml','250cal per serving','100cal per serving','200cal per 100ml'),tags='child')
            my_tree.insert(4,index='end',iid=(a+4),values=('','7cal per almond','112cal per 100ml','200cal per 100ml','250cal per serving','50cal per 25g','250 cal per 100 ml'),tags='child')
            my_tree.insert(5,index='end',iid=(a+5),values=('','7cal per almond','100cal per serving','19cal per 100ml','100cal per 100g','50cal per 25g','200cal per serving'),tags='child')
            my_tree.insert(6,index='end',iid=(a+6),values=('','7cal per almond','250cal per 100ml','19cal per 100ml','200cal per serving','100cal per 50g','200cal per serving'),tags='child')
    
            my_tree.tag_configure('child',background='#DACEB7' )
            my_tree.pack()
            tree_scroll.config(command=my_tree.yview)
    
            l8=Label(top,text="your total colorie intake per week = 2500 x 7 cal = 17,500 cal")
            l8.pack(anchor=CENTER)
            top.mainloop()

        root = Tk()
        root.title('diet plan')
        # style= root.Style()
        # style.theme_use('clam')
        b1=Button(root, text="Weight loss",command=open_wl).pack(pady=20)
        b2=Button(root, text='Weight gain',command=open_wg).pack(pady=20)
        root.mainloop()

    button1=Button(new_window,text="BMI Tracker",width=20,height=10,background="black",foreground="white")
    button1.config(command=button1_clicked)
    button1.config(font=("Arieal",12,"bold"))
    button1.place(x=1200,y=40)

    button2=Button(new_window,text="Calorie Tracker",width=20,height=10,background="black",foreground="white")
    button2.config(command=button2_clicked)
    button2.config(font=("Arieal",12,"bold"))
    button2.place(x=1200,y=280)

    button3=Button(new_window,text="Diet Tracker",width=20,height=10,background="black",foreground="white")
    button3.config(command=button3_clicked)
    button3.config(font=("Arieal",12,"bold"))
    button3.place(x=1200,y=510)
    new_window.mainloop()


my_button=Button(text="Yes2LiveHealthy",font=("Comic Sans MS",15,"bold"),command=button_clicked)
my_button.place(x=700,y=600)
window.mainloop()