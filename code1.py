from tkinter import *
from tkinter import ttk

def open_wl():
    top=Toplevel()
    top.title("Weight loss")
    my_tree=ttk.Treeview(top)
    my_tree['columns']=('Day','food_pre_breakfast','food_breakfast','food_pre_lunch','food_lunch','food_snacks', 'food_dinner')

    my_tree.column("#0", width=0,  stretch=NO)
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
        ['2','Cucumber Detox Water','Curd, Mixed Vegetable Stuffed Roti','Mixed Vegetable salad','Lentil Curry,Methi Rice','Apple,buttermillk','Sauteed Vegetables with Paneer,Roti'],
        ['3','Cucumber Detox Water','Skim Milk Yoghurt, Multigrain Toast','Skimmed Milk Paneer','Sauteed Vegetables with Paneer,Roti','Banana,Buttermilk','Lentil Curry, Methi Rice'],
        ['4','Cucumber Detox Water','Fruit and Nuts Yogurt Smoothie','Mixed Vegetable Salad','Green Gram Whole Dal Cooked,Bhindi sabzi','Orange, Buttermilk','Palak Chole, Steamed Rice'],
        ['5','Cucumber Detox Water','Skimmed Milk, Peas Poha','Skimmed Milk Paneer','Low Fat Paneer Curry, Missi Roti','Papaya, Buttermilk','Curd, Aloo Baingan Tamatar Ki Sabzi'],
        ['6','Cucumber Detox Water','Mixed Sambar, Idli','Mixed Vegetable Salad','Curd, Aloo Baingan Tamatar Ki Sabzi','Cut Fruits, Buttermilk','Green Gram Whole Dal Cooked, Bhindi sabzi'],
        ['7','Cucumber Detox Water','Besan Chilla','Skimmed Milk Paneer','Palak Chole, Steamed Rice','Apple, Buttermilk','Low Fat Paneer Curry, Missi Roti']
    ]

    count=0
    for i in food:
        my_tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        count+=1
    
    my_tree.pack()

def open_wg():
    top=Toplevel()
    top.title("Weight gain")
    my_tree=ttk.Treeview(top)
    my_tree['columns']=('Day','food_pre_breakfast','food_breakfast','food_pre_lunch','food_lunch','food_snacks', 'food_dinner')

    my_tree.column("#0", width=0,  stretch=NO)
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
        [1,'Cucumber Detox Water','Oats Porridge in Skimmed Milk','Skimmed Milk Panner','Dal,Gajar Matar Sabzi,Roti','Cut Fruits, Buttermilk','Dal,Lauki Sabzi,Roti'],
        [2,'Cucumber Detox Water','Curd, Mixed Vegetable Stuffed Roti','Mixed Vegetable salad','Lentil Curry,Methi Rice','Apple,buttermillk','Sauteed Vegetables with Paneer,Roti'],
        [3,'Cucumber Detox Water','Skim Milk Yoghurt, Multigrain Toast','Skimmed Milk Paneer','Sauteed Vegetables with Paneer,Roti','Banana,Buttermilk','Lentil Curry, Methi Rice'],
        [4,'Cucumber Detox Water','Fruit and Nuts Yogurt Smoothie','Mixed Vegetable Salad','Green Gram Whole Dal Cooked,Bhindi sabzi','Orange, Buttermilk','Palak Chole, Steamed Rice'],
        [5,'Cucumber Detox Water','Skimmed Milk, Peas Poha','Skimmed Milk Paneer','Low Fat Paneer Curry, Missi Roti','Papaya, Buttermilk','Curd, Aloo Baingan Tamatar Ki Sabzi'],
        [6,'Cucumber Detox Water','Mixed Sambar, Idli','Mixed Vegetable Salad','Curd, Aloo Baingan Tamatar Ki Sabzi','Cut Fruits, Buttermilk','Green Gram Whole Dal Cooked, Bhindi sabzi'],
        [7,'Cucumber Detox Water','Besan Chilla','Skimmed Milk Paneer','Palak Chole, Steamed Rice','Apple, Buttermilk','Low Fat Paneer Curry, Missi Roti']
    ]

    count=0
    for i in food:
        my_tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        count+=1
    
    my_tree.pack()
root = Tk()
root.title('diet plan')

b1=Button(root, text="Weight loss",command=open_wl).grid(row=0, column=0)
b2=Button(root, text='Weight gain',command=open_wg).grid(row=0, column=1)

root.mainloop()
