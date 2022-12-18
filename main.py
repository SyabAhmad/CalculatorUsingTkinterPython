from tkinter import *

main_window = Tk()

Label(main_window, text="Hey This is Syab Ahmad de Developer").grid(row=0, column=1)
Label(main_window, text="Enter First Number: ").grid(row=1, column=0)
Label(main_window, text="Enter First Number: ").grid(row=2, column=0)
num1 = Entry(main_window, width=20, borderwidth=5)
num1.grid(row=1, column=1)
num2 = Entry(main_window, width=20, borderwidth=5)
num2.grid(row=2, column=1)

def on_Click():
    sum = int(num1.get()+num2.get())

    Label(main_window, text=sum).grid(row=3, column=2)

Button(main_window, text="Find Sum", command= on_Click).grid(row=4, column=1)
Label(main_window, text="de Developer").grid(row=5, column=3)


main_window.mainloop()