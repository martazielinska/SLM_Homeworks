import tkinter as tk
from tkinter import *
from tkinter import messagebox



def primenumbers():
    txt.delete('1.0',END)
    try:
        N=int(E.get())
        primelist=list()
        upperbound=52

        while len(primelist)<N:
             for number in range(upperbound-50, upperbound):
                prime = True
                for i in range(2, upperbound):
                    if (i!=number):
                        if (number % i == 0):
                            prime = False
                if prime:

                    primelist.append(number)
             upperbound+=50

        primelist=primelist[:N]
        print(len(primelist))
        txt.insert(INSERT, primelist)
        txt.pack()
        messagebox.showinfo("Success", "Your numbers are ready.")
    except:
        messagebox.showerror("Error", "Please try a different input.")




root = tk.Tk(className='Prime numbers printer')
root.geometry('500x500')
root.configure(bg='#001233')

tk.Label(root, text="Insert the number of prime numbers you want to print", bg='#001233', fg='#ffffff', font=('Calibri Light', '13')).pack()
E=tk.Entry(root)
E.pack()
tk.Button(root, text='Print Prime Numbers', command=primenumbers, bg='#eb5e28', fg='#ffffff',font=('Calibri Light', '12')).pack(side=BOTTOM)
txt=tk.Text(root,bg='#33415c', fg='#ffffff')




root.mainloop()