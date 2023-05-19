
my_list = ['Curso 1','Curso 2'] # create a  list 
import tkinter as tk
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("300x150")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title
my_list2=[] 
def my_upd(*args):
    cb2.set('') # remove the previous selected option 
    my_list2 = ['Juan','Pedro','Rosa'] # create a  list 
    cb2['values']=my_list2
    
sel=tk.StringVar()

cb1 = ttk.Combobox(my_w, values=my_list,width=15,textvariable=sel)
cb1.grid(row=1,column=1,padx=30,pady=30)

sel.trace('w',my_upd) # track the change event 

cb2 = ttk.Combobox(my_w, values=my_list2,width=15)
cb2.grid(row=1,column=2)

my_w.mainloop()  # Keep the window open