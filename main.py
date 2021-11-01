from tkinter import *
from tkinter import ttk
import igscrap
from PIL import Image, ImageTk
from threading import Thread

class MyApp():
    def __init__(self,root):
        #style = ttk.Style(root)
        #current_theme = style.theme_use('clam')

        root.title('YT analyser')
        root.resizable(False,False)

        self.frm = ttk.Frame(root,padding=100,height=30,width=30)
        self.frm.grid()  

        lbl = ttk.Label(self.frm, text="YouTube analyser",padding=10)
        lbl.config(font=('Arial',30))
        lbl.grid(row=1)


        self.entry_text = StringVar()
        textbox = ttk.Entry(self.frm, textvariable=self.entry_text)
        textbox.grid(row=2,pady=10)


        btn = ttk.Button(self.frm, text="Analyse",command=self.openNewWindow)
        btn.grid(row=3)

        lbl1 = ttk.Label(self.frm,text="Leave blank to analyse /trending or type your youtuber's nickname")
        lbl1.config(font=('Arial',7))
        lbl1.grid(row=4) 

        self.pgb = ttk.Progressbar(self.frm,orient='horizontal',mode='indeterminate',length=280)      


 


    def openNewWindow(self):
        self.pgb.grid(row=5,pady=10)
        self.pgb.start()
        newWindow = Toplevel(root)
        newWindow.title("New Window")
        scrap_thread = igscrap.DriverEngine()
        scrap_thread.start()
        self.monitor(scrap_thread)  
        

    def monitor(self, thread):
        if not thread.is_alive():
            self.pgb.grid_forget()

            


root = Tk()
MyApp(root)
root.mainloop()