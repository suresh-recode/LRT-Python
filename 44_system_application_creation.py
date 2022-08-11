from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry('950x500')
win.title("LRT - Sample Application")
win.iconbitmap('recode.ico')
top_label = Label(win, text="Addition of two number", font=('Calibri 15 bold'))
top_label.place(x=400, y=10)


def add_value():
    global val1_text_box, val2_text_box
    try:
        total = int(val1_text_box.get("1.0", "end-1c")) + \
                int(val2_text_box.get("1.0", "end-1c"))
        messagebox.showinfo("Result", "The given value are : {0} and {1}. The sum is {2}".format(
            val1_text_box.get("1.0", "end-1c"),  val2_text_box.get("1.0", "end-1c"), total
        ))
    except:
        messagebox.showerror("Error", "Value should be integer")


val1_label = Label(win, text="Enter value 1: ", font=('Calibri 15'))
val1_label.place(x=30, y=50)
val1_text_box = Text(
    win,
    height=1,
    width=20,
    font=('Calibri 13')
)
val1_text_box.place(x=180, y=50)
val1_label = Label(win, text="Enter value 2: ", font=('Calibri 15'))
val1_label.place(x=30, y=90)
val2_text_box = Text(
    win,
    height=1,
    width=20,
    font=('Calibri 13')
)
val2_text_box.place(x=180, y=90)
add_button = Button(win, text="Add value", font=('Calibri 10'),
                    command=lambda: add_value())
add_button.place(x=100, y=150)
win.mainloop()