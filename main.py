from tkinter import *
from tkinter import ttk

root = Tk()

style = ttk.Style(root)
current_theme = style.theme_use('clam')

root.title('YT analyser')
root.resizable(False,False)

def openNewWindow():
    newWindow = Toplevel(root)
    newWindow.title("New Window")


frm = ttk.Frame(root,padding=100,height=30,width=30)
frm.grid()

lbl = ttk.Label(frm, text="YouTube analyser",padding=10)
lbl.config(font=('Arial',30))
lbl.grid(column=0, row=0)



textbox = ttk.Entry(frm)
textbox.grid(column=0,row=1,pady=10)


btn = ttk.Button(frm, text="Analyse",command=openNewWindow)
btn.grid(column=0, row=2)

lbl1 = ttk.Label(frm,text="Leave blank to analyse /trending or type your youtubers' nickname")
lbl1.config(font=('Arial',7))
lbl1.grid(row=3)




root.mainloop()