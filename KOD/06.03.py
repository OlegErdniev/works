from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *




def clicked():
    res = "Privet {}".format(txt.get())
    lbl.configure(text=res)
def click():
    lbl1.configure(text=selected.get())
window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('800x250')

txt1 = scrolledtext.ScrolledText(window,width = 40, height = 10)
txt1.grid(column=0,row=2)

selected = IntVar()
rad1 = Radiobutton(window,text='First', value = 1, variable=selected)
rad2 = Radiobutton(window,text='Second', value = 2, variable=selected)
rad3 = Radiobutton(window,text='Third', value = 3, variable=selected)
rad1.grid(column=0,row=1)
rad2.grid(column=1,row=1)
rad3.grid(column=2,row=1)
lbl1 = Label(window)
lbl1.grid(column = 0,row=2)
btn1 = Button(window,text="Click", command=click)
btn1.grid(column = 3,row=1)


chk_state = BooleanVar()
chk_state.set(False)
chk = Checkbutton(window, text="Choose", var=chk_state)
chk.grid(column=4, row=0)


combo = Combobox(window)
combo["values"] = (1, 2, 3, 4, 5,"Text")
combo.current(1)
combo.grid(column=3, row=0)


lbl = Label(window, text="Привет", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)


btn = Button(window, text="Не нажимать!", command=clicked)
btn.grid(column=2, row=0)


txt = Entry(window, width=10,state='disabled')
txt.grid(column=1, row=0)
txt.focus()

window.mainloop()
