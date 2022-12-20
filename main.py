import this
from tkinter import *
main_window = Tk()
main_window.title("Calculator Using Python")
Label(main_window, text="Hey This is Syab Ahmad de Developer").grid(row=0, column=1)
Label(main_window, text="Enter First Number: ").grid(row=1, column=0)
Label(main_window, text="Enter First Number: ").grid(row=2, column=0)
num1 = Entry(main_window, width=20, borderwidth=5)
num1.grid(row=1, column=1)
num2 = Entry(main_window, width=20, borderwidth=5)
num2.grid(row=2, column=1)

def on_Click():
    sum = int(num1.get()) + int(num2.get())

    Label(main_window, text=sum).grid(row=3, column=2)

Button(main_window, text="Find Sum", command= on_Click).grid(row=4, column=1)
Label(main_window, text="de Developer").grid(row=5, column=3)


main_window.mainloop()



# class displayShow:
#
#     def nine(self):
#         pass
#     def eight(self):
#         pass
#     def seven(self):
#         pass
#     def six(self):
#         pass
#     def five(self):
#         pass
#     def four(self):
#         pass
#     def three(self):
#         pass
#     def two(self):
#         pass
#     def one(self):
#         pass
#
#     def show(self):
#         Button(main_window, text="9",).grid(row=7, column=5)
#         Button(main_window, text="8",).grid(row=7, column=4)
#         Button(main_window, text="7",).grid(row=7, column=3)
#         Button(main_window, text="6",).grid(row=8, column=5)
#         Button(main_window, text="5",).grid(row=8, column=4)
#         Button(main_window, text="4",).grid(row=8, column=3)
#         Button(main_window, text="3",).grid(row=9, column=5)
#         Button(main_window, text="2",).grid(row=9, column=4)
#         Button(main_window, text="1",).grid(row=9, column=3)
