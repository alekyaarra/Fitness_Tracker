from tkinter import *
from tkinter import ttk

def weight_loss():
    my_tree=ttk.Treeview(root)
    my_tree['columns']=('food_pre_breakfast','food_breakfast','food_pre_lunch','food_lunch','food_snacks', 'food_dinner')

    my_tree.column("#0", width=0,  stretch=NO)
    my_tree.column("food_pre_breakfast",anchor=CENTER, width=150)
    my_tree.column("food_breakfast",anchor=CENTER, width=150)
    my_tree.column("food_pre_lunch",anchor=CENTER, width=150)
    my_tree.column("food_lunch",anchor=CENTER, width=150)
    my_tree.column("food_snacks",anchor=CENTER, width=150)
    my_tree.column("food_dinner",anchor=CENTER, width=300)
    
    my_tree.heading("#0", text='', anchor=CENTER)
    my_tree.heading("food_pre_breakfast",text="Pre Breakfast", anchor=CENTER)
    my_tree.heading("food_breakfast",text='Breakfast', anchor=CENTER)
    my_tree.heading("food_pre_lunch",text='Pre Lunch', anchor=CENTER)
    my_tree.heading("food_lunch",text='Lunch', anchor=CENTER)
    my_tree.heading("food_snacks",text='Snacks', anchor=CENTER)
    my_tree.heading("food_dinner",text='Dinner', anchor=CENTER)

    food=[
        ['Cucumber Detox Water','Oats Porridge in Skimmed Milk','Skimmed Milk Panner','Dal,Gajar Matar Sabzi,Roti','Cut Fruits, Buttermilk','Dal,Lauki Sabzi,Roti'],
        ['Cucumber Detox Water','Curd, Mixed Vegetable Stuffed Roti','Mixed Vegetable salad','Lentil Curry,Methi Rice','Apple,buttermillk','Sauteed Vegetables with Paneer,Roti'],
        ['Cucumber Detox Water','Skim Milk Yoghurt, Multigrain Toast','Skimmed Milk Paneer','Sauteed Vegetables with Paneer,Roti','Banana,Buttermilk','Lentil Curry, Methi Rice'],
        ['Cucumber Detox Water','Fruit and Nuts Yogurt Smoothie','Mixed Vegetable Salad','Green Gram Whole Dal Cooked,Bhindi sabzi','Orange, Buttermilk','Palak Chole, Steamed Rice'],
        ['Cucumber Detox Water','Skimmed Milk, Peas Poha','Skimmed Milk Paneer','Low Fat Paneer Curry, Missi Roti','Papaya, Buttermilk','Curd, Aloo Baingan Tamatar Ki Sabzi'],
        ['Cucumber Detox Water','Mixed Sambar, Idli','Mixed Vegetable Salad','Curd, Aloo Baingan Tamatar Ki Sabzi','Cut Fruits, Buttermilk','Green Gram Whole Dal Cooked, Bhindi sabzi'],
        ['Cucumber Detox Water','Besan Chilla','Skimmed Milk Paneer','Palak Chole, Steamed Rice','Apple, Buttermilk','Low Fat Paneer Curry, Missi Roti']
    ]

    count=0
    for i in food:
        my_tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        count+=1
    
    my_tree.pack()


root = Tk()
root.state("zoomed")
root.title('diet plan')

#my_tree=ttk.Treeview(root)
b1=Button(root, text="Weight loss",command=weight_loss).pack()
b2=Button(root, text='Weight gain').pack()

root.mainloop()



